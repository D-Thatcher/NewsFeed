from PyQt5 import QtGui, QtWidgets,QtCore
from NewsFeed import Ui_MainWindow
import sys
import webbrowser
import Util
import threading
import time
from Sentiment import Sentient
import numpy as np
from nltk.tokenize import RegexpTokenizer
from Constants import RSS_FEED_GENERAL, TWITTER_INTERESTED, SUBREDDIT_INTERESTED, month_lst,remove_if_present
from RSSParser import preset_highlight
from Influx import News



class ApplicationWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        super(ApplicationWindow, self).__init__()
        self.setupUi(self)

        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setRootIsDecorated(False)

        self.entries = []
        self.entries_fam = []
        self.lo_link = []

        self.hashed_title = set()

        # Load preset filters here
        self.filters = []

        self.do_sentiment = True
        self.sentient = None
        self.sentient_score = []

        if self.do_sentiment:
            self.sentient = Sentient()

        self.preset_highlight = preset_highlight
        self.highlights = []

        self.highlight_bool = []
        self.COLOUR = (128, 169, 237)
        self.highlight_colour = []

        self.rss_feed=[]
        self.news_influx = News()


        self.treeWidget.itemDoubleClicked.connect(self.handler)

        self.font_top = None
        self.font_child = None
        self.font_disconnect = None

        self.font_sz = 22
        self.load_font()

        self.liveUpdateBox.setChecked(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)

        self.main_frame_width = self.frameGeometry().width()
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        gui = self.frameGeometry()


        self.treeWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.treeWidget.setFrameShape(QtWidgets.QFrame.NoFrame)

        # 1 update every 10 seconds on live mode
        self.period = 10

        # Load Settings and Companies
        # self.remove, self.highlight_preset = ReadCompanies.get_settings()
        #
        # self.all_ticker, self.first_for_search, self.idx_hash, self.all_non_exchange, self.two_for_search = ReadCompanies.ticker_map_et_all()
        self.tokenizer = RegexpTokenizer(r'\w+')

        self.include_twitter = True
        self.include_reddit = True

        self.update_entries()
        self.repopulate()

        self.live_thread_running = False
        self.live_thread = threading.Thread(target=self.wait_update)

        self.updateButton.clicked.connect(self.update_click)
        self.liveUpdateBox.stateChanged.connect(self.update_live)

        self.presetHighlightBox.setChecked(True)
        self.presetHighlightBox.stateChanged.connect(self.preset_update)


        self.twitterBox.setChecked(self.include_twitter)
        self.twitterBox.stateChanged.connect(self.twitter_update)

        self.redditBox.setChecked(self.include_reddit)
        self.redditBox.stateChanged.connect(self.reddit_update)


        self.showButton.clicked.connect(self.hide_frame)
        self.hideButton.clicked.connect(self.show_frame)

        self.searchBar.textChanged.connect(self.no_enter_empty_search)
        self.highlightBar.textChanged.connect(self.no_enter_empty_highlight)
        #self.keyPressed.connect(self.on_key_pressed)

        self.screen_sizing(screen)


    def screen_sizing(self,screen):
        GRACE = 20
        self.showMaximized()
        self.scrollArea.resize(screen.width() - GRACE, screen.height() - GRACE)
        self.treeWidget.resize(screen.width() - GRACE, screen.height() - GRACE)

        self.frame.setGeometry(0, screen.height() - self.frame.frameGeometry().height() - 75,
                               self.frame.frameGeometry().width(), self.frame.frameGeometry().height())
        vw = self.frameButton.frameGeometry().width()
        vh = self.frameButton.frameGeometry().height()
        self.frameButton.setGeometry(screen.width() - vw - 18, screen.height() - vh - 100, vw, vh)
        self.frameButton.setStyleSheet("background-color:none")

        op = QtWidgets.QGraphicsOpacityEffect(self)
        op.setOpacity(0.99)
        self.frame.setGraphicsEffect(op)
        self.frame.setAutoFillBackground(True)

        self.not_hidden_scroll_area_height = self.scrollArea.frameGeometry().height()
        self.not_hidden_frame_area_height = self.scrollArea.frameGeometry().height()

        self.hidden_scroll_area_height = self.not_hidden_scroll_area_height + self.not_hidden_frame_area_height
        self.hidden_frame_area_height = 0

    def twitter_update(self,event):
        self.include_twitter = self.twitterBox.isChecked()
        self.update_click(True)

    def reddit_update(self,event):
        self.include_reddit = self.redditBox.isChecked()
        self.update_click(True)

    def preset_update(self,event):
        c = self.presetHighlightBox.isChecked()
        if not c:
            self.preset_highlight = []
        else:
            self.preset_highlight = preset_highlight

        self.update_click(True)

    def resize_hidden(self,hidden):
        if hidden:
            self.scrollArea.setFixedHeight(self.hidden_scroll_area_height)
            self.treeWidget.setFixedHeight(self.hidden_scroll_area_height)
        else:
            self.scrollArea.setFixedHeight(self.not_hidden_scroll_area_height)
            self.treeWidget.setFixedHeight(self.not_hidden_scroll_area_height)


    def show_frame(self, event):
        self.resize_hidden(0)
        self.frame.setHidden(0)

    def hide_frame(self, event):
        self.resize_hidden(1)
        self.frame.setHidden(1)


    # Returns the best matching full company name from the partial match and True,
    # otherwise returns the partial and False: WC: O(number_of_companies), AV: O(1)
    def best_match_full_company(self, partial, tokenized):
        tokenizer = self.tokenizer
        p_tokenized = tokenizer.tokenize(partial.lower())[0]
        if p_tokenized not in self.first_for_search:
            return partial, False

        idc = self.idx_hash[p_tokenized]

        store_num_match = []
        # number of matches
        for j in idc:
            attempt = self.all_non_exchange[j].lower()
            att_tokens = tokenizer.tokenize(attempt)
            num_matches = 0

            for i in att_tokens:
                if i in tokenized:
                    num_matches+=1

            store_num_match.append(num_matches)

        mx = max(store_num_match)

        matches = []
        for k in range(0,len(store_num_match)):
            if store_num_match[k]==mx:
                matches.append(self.all_non_exchange[idc[k]])

        return matches

    def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_Return:
            self.highlight_action(self.highlightBar.text())
            self.search_action(self.searchBar.text())

    def no_enter_empty_search(self,text):
        if len(text) == 0:
            self.filters = []
            self.update_click(True)

    def no_enter_empty_highlight(self,text):
        if len(text) == 0:
            self.highlights = []
            self.update_click(True)

    def highlight_action(self, text):
        if len(text) == 0:
            self.highlights = []
        else:
            self.parse_search(text, True)
        self.update_click(True)

    def search_action(self, text):
        if len(text) == 0:
            self.filters = []
        else:
            self.parse_search(text)
        self.update_click(True)

    # Returns a list of filters. Input text is a comma-seperated list of filters
    def parse_search(self, text, highlight=False):
        text = self.massage_contents(text)
        parse_fields = text.split(",")
        parse_fields = [i.strip() for i in parse_fields if (len(i) > 0) and (i != len(i) * ' ')]

        if not highlight:
            self.filters = parse_fields
        else:
            self.highlights = parse_fields



    def wait_update(self):
        self.update_click()
        tick = time.time()

        while self.live_thread_running:
            if (time.time()-tick) > self.period:
                self.update_click()
                tick = time.time()


    def update_click(self, static=False):
        self.update_entries(static)
        self.repopulate()

    def update_live(self):

        if not self.live_thread_running:
            self.live_thread_running= True
            self.updateButton.setDisabled(True)
            self.live_thread.start()
        else:
            self.live_thread_running = False
            while self.live_thread.is_alive():
                pass
            self.live_thread = None
            self.live_thread = threading.Thread(target=self.wait_update)
            self.updateButton.setDisabled(False)

    def date_portion(self, date):
        if '-' in date and date[0] == '2':
            splt = date.split(' ')[0]
            splt = splt.split('-')
            if len(splt) > 2:
                year = splt[0]
                mo = splt[1]
                day = splt[2]
                return month_lst[int(mo) - 1][:3] + " " + str(int(day)) + ", " + year
            else:
                return date
        else:
            splt = date.split(' ')[:3]
            return splt[0] + " " + splt[1] + " " + splt[2]

    # Only ends line at end of a word
    def fill_summary_with_wrap(self, summary, width):
        if len(summary)<2:return summary

        if '\n' in summary:
            summary = summary.replace('\n',' ')

        new_summary = summary[0]
        in_debt = False
        for i in range(1, len(summary)):
            if i % width == 0 or in_debt:
                if summary[i] == ' ':
                    new_summary += '\n'
                    in_debt = False
                else:
                    new_summary += summary[i]
                    in_debt = True
            else:
                new_summary += summary[i]
        return new_summary

    def process_item(self,item, highlight_item=False, colour=None, contents=""):
        if 'title' in item:
            self.highlight_bool.append(highlight_item)
            self.highlight_colour.append(colour)

            if 'summary' in item:
                self.entries_fam.append(self.fill_summary_with_wrap(item['summary'], 110))
            else:
                self.entries_fam.append(" ")

            if 'published' in item:
                try:
                    self.entries.append(self.date_portion(item['published']) + "   " + item['title'])
                except Exception as e:
                    print(item)
                    print(item['title'])
                    print(item['link'])
                    assert(False)

                prev = self.entries_fam.pop()

                if not (item['reddit'] or item['twitter']):
                    self.entries_fam.append(item['published'] + "\n\n" + prev)
                else:
                    self.entries_fam.append(item['full date'] + "\n\n" + prev)


            else:
                self.entries.append(item['title'])

            if 'link' in item:
                self.lo_link.append(item['link'])
            else:
                self.lo_link.append("")

            if len(contents)>0:
                self.sentient_score.append(str(self.sentient.process_paragraph(contents)))

                # print(self.sentient_score[-1])




    def refresh(self):
        self.hashed_title = set()
        self.entries = []
        self.sentient_score = []
        self.entries_fam = []
        self.lo_link = []
        self.highlight_bool = []
        self.highlight_colour = []

    def update_rss(self, static):
        self.news_influx.include_twitter = self.include_twitter
        self.news_influx.include_reddit = self.include_reddit

        if not static:
            self.rss_feed = self.news_influx.update_information(rss_urls=RSS_FEED_GENERAL,twitter_users=TWITTER_INTERESTED,subreddit_names=SUBREDDIT_INTERESTED)
            #self.rss_feed = RSSParser.get_feed(RSS_FEED_GENERAL)


    def build_contents(self,item):
        contents = ""
        if 'title' in item:
            contents += item['title'] + " "
            if 'summary' in item:
                contents += item['summary']

        return self.massage_contents(contents), contents

    def update_entries(self, static=False):
        self.refresh()
        self.update_rss(static)

        for item in self.rss_feed:
            contents, raw_contents = self.build_contents(item)
            hash_title = item['title'].lower().strip()
            proceed = (hash_title not in self.hashed_title)
            proceed_if_reddit = item['reddit'] and self.include_reddit
            proceed_if_twitter = item['twitter'] and self.include_twitter
            proceed_if_rss = not(item['reddit'] or item['twitter'])
            proceed_if_no_garbage = all([i not in contents for i in remove_if_present])
            self.hashed_title.add(hash_title)
            proceed = proceed and (proceed_if_reddit or proceed_if_twitter or proceed_if_rss) and proceed_if_no_garbage
            if len(contents) > 0 and proceed:

                filter_text_in_contents = False
                highlight_text_in_contents = False
                colour = None
                combo_highlight = self.preset_highlight + self.highlights

                if len(self.filters) > 0:
                    for f_text in self.filters:
                        if f_text in contents:
                            filter_text_in_contents = True
                    for i_h_text in range(0,len(combo_highlight)):

                        if combo_highlight[i_h_text] in contents:

                            highlight_text_in_contents = True
                            colour = self.COLOUR


                    if filter_text_in_contents:
                        self.process_item(item, highlight_text_in_contents, colour,contents=contents)

                else:
                    for i_h_text in range(0, len(combo_highlight)):

                        if combo_highlight[i_h_text] in contents:

                            highlight_text_in_contents = True

                            colour = self.COLOUR

                    self.process_item(item, highlight_text_in_contents,colour,contents=contents)

    def massage_contents(self,contents):
        contents = contents.lower()
        contents = contents.strip()
        return contents.replace('.', '')

    def load_font(self):
        self.font_top = QtGui.QFont()
        self.font_top.setFamily("Helvetica")  # Times New Roman,Arial
        self.font_top.setBold(True)
        self.font_top.setPointSize(self.font_sz)

        self.font_child = QtGui.QFont()
        self.font_child.setFamily("Helvetica")  # Times New Roman,Arial
        self.font_child.setBold(False)
        self.font_child.setPointSize(15)

        self.font_disconnect = QtGui.QFont()
        self.font_disconnect.setFamily("Helvetica")  # Times New Roman,Arial
        self.font_disconnect.setBold(True)
        self.font_disconnect.setPointSize(self.font_sz*2)

    def icon_from_rgb(self,rgb):
        im_np = np.zeros((100, 100, 3), dtype=np.uint8)
        im_np[:, :, 0] = rgb[0]
        im_np[:, :, 1] = rgb[1]
        im_np[:, :, 2] = rgb[2]
        # im_np = np.transpose(im_np, (1, 0, 2)).copy()

        qimage = QtGui.QImage(im_np, im_np.shape[1], im_np.shape[0],
                              QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap(qimage)
        icon = QtGui.QIcon()
        icon.addPixmap(pixmap)
        return icon

    def repopulate(self):
        self.treeWidget.clear()
        num_entries = len(self.entries)

        if num_entries==0:
            if not Util.internet_on():
                item = QtWidgets.QTreeWidgetItem(self.treeWidget)
                item.setText(0, "Internet Disconnected")
                item.setFont(0, self.font_disconnect)
            else:
                item = QtWidgets.QTreeWidgetItem(self.treeWidget)
                item.setText(0, "")

        for i in range(0,num_entries):
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            item.setText(0,self.entries[i])

            if self.do_sentiment:
                rgb = self.sentient.rgb_from_score(self.sentient_score[i])
                icon = self.icon_from_rgb(rgb)
                item.setIcon(0,icon)


            sz = QtCore.QSize()
            sz.setHeight(int(100*(self.font_sz/22)))
            item.setSizeHint(0,sz)

            child = QtWidgets.QTreeWidgetItem(item)
            child.setText(0, self.entries_fam[i])

            child.setFont(0,self.font_child)
            item.setFont(0,self.font_top)


            if self.highlight_bool[i]:
                item.setBackground(0, QtGui.QColor(*self.highlight_colour[i]))
            elif i % 2 == 0:
                item.setBackground(0,QtGui.QColor(237, 240, 244))

    def handler(self, item, column_no):

        idx = self.treeWidget.indexOfTopLevelItem(item)
        idx_from_child = self.treeWidget.indexOfTopLevelItem(item.parent())

        if idx == -1:
            self.go_to_article(self.lo_link[idx_from_child])

    def go_to_article(self, link):
        if len(link)>0:
            webbrowser.open(link)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = ApplicationWindow()
    window.show()
    sys.exit(app.exec_())