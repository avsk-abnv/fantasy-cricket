from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3,json,random,math,new_match
def newTeam_dialog(self,act,select=0) :
    if act=="open":
        self.widget_3.show()
        self.widget.setEnabled(False)
        self.widget_2.setEnabled(False)
        self.menubar.setEnabled(False)
        self.lineEdit.setFocus(True)
    elif act=="close":
        self.widget_3.hide()
        self.widget.setEnabled(True)
        self.widget_2.setEnabled(True)
        self.menubar.setEnabled(True)
        if select==1 and len(self.lineEdit.text())>0:
            self.label_11.setText(self.lineEdit.text())
            self.cancelButton.show()

def openteam(self,act,select=0):
    if act=="open":
        self.widget_7.show()
        self.widget.setEnabled(False)
        self.widget_2.setEnabled(False)
        self.menubar.setEnabled(False)
        self.cur_players.execute("select name from teams")
        t_list=self.cur_players.fetchall()
        self.comboBox_3.clear()
        for team in t_list:
                self.comboBox_3.addItem(team[0])

    elif act=="close":
        self.widget_7.hide()
        self.widget.setEnabled(True)
        self.widget_2.setEnabled(True)
        self.menubar.setEnabled(True)
        if select==1:
            self.label_11.setText(self.comboBox_3.currentText())
            self.cur_players.execute("select players,value from teams where name like ?;",(self.comboBox_3.currentText(),))
            result= self.cur_players.fetchone()
            player_list=json.loads(result[0])
            team_value=result[1]
            ctg_BAT=0
            ctg_BWL=0
            ctg_AR=0
            ctg_WK=0
            self.listWidget_2.clear()
            for player in player_list:
                self.cur_players.execute("select ctg from stats where player like ?;",(player,))
                result=self.cur_players.fetchone()
                ctg=result[0]
                if ctg=="BAT":
                    ctg_BAT=ctg_BAT+1
                elif ctg=="BWL":
                    ctg_BWL=ctg_BWL+1
                elif ctg=="AR":
                    ctg_AR=ctg_AR+1
                elif ctg=="WK":
                    ctg_WK=ctg_WK+1
                item=QtWidgets.QListWidgetItem(player)
                self.listWidget_2.addItem(item)
            self.label_6.setText(str(ctg_BAT))
            self.label_7.setText(str(ctg_BWL))
            self.label_8.setText(str(ctg_AR))
            self.label_9.setText(str(ctg_WK))
            self.label_13.setText(str(team_value))
            self.label_15.setText(str(1000-team_value))
            self.cancelButton.show()

def show_evteam(self,act) :
    if act==1:
        self.widget_4.show()
        self.widget.setEnabled(False)
        self.widget_2.setEnabled(False)
        self.menubar.setEnabled(False)
        self.cur_players.execute("select name from teams")
        t_list=self.cur_players.fetchall()
        self.comboBox_2.clear()
        self.comboBox.clear()
        for team in t_list:
                self.comboBox_2.addItem(team[0])
        self.cur_players.execute("select match_id from match_played")
        match_list=self.cur_players.fetchall()
        for match in match_list:
            self.comboBox.addItem(match[0])
        self.comboBox.addItem("+ Play a New Match")
        self.reset_everything()
        self.listWidget_3.clear()
        team_name=self.comboBox_2.currentText()
        self.cur_players.execute("select players from teams where name like ?;",(team_name,))
        get_players=self.cur_players.fetchone()
        player_str=get_players[0]
        player_list=json.loads(player_str)
        for player in player_list:
            self.listWidget_3.addItem(player)
        self.listWidget_4.clear()
        for i in range(len(player_list)):
            self.listWidget_4.addItem("0")
    elif act==2:
        self.widget_4.hide()
        self.widget.setEnabled(True)
        self.widget_2.setEnabled(True)
        self.menubar.setEnabled(True)

def save_team(self,act) :
    if act=="open":
        if self.label_11.text()=="---":
            error_dialog(self,"open","Nothing to be Saved !!")
        elif self.listWidget_2.count()<11:
            error_dialog(self,"open","A Cricket Team has 11 players")
        elif int(self.label_9.text())==0:
            error_dialog(self,"open","Select at least one Wicktet-Keeper")
        elif int(self.label_7.text())+int(self.label_8.text())<5:
            error_dialog(self,"open","Bowlers + Allrounders should be at least 5")

        else:
            list=[]
            for i in range(self.listWidget_2.count()):
                list.append(self.listWidget_2.item(i).text())
            player_list=json.dumps(list)
            self.cur_players.execute("select * from teams where name like ?;",(self.label_11.text(),))
            result=self.cur_players.fetchall()
            if len(result)>0:
                self.cur_players.execute("update teams set players=?,value=? where name=?;"
                ,(player_list,int(self.label_13.text()),self.label_11.text()))
                self.myplayers.commit()
                self.widget_5.show()
                self.widget.setEnabled(False)
                self.widget_2.setEnabled(False)
                self.menubar.setEnabled(False)
                self.reset_everything()
            else:
                self.cur_players.execute("select count(*) from teams")
                carr=self.cur_players.fetchone()
                count=carr[0]
                self.cur_players.execute("insert into teams (name,players,value) values (?,?,?);",
                (self.label_11.text(),player_list,int(self.label_13.text())))
                self.myplayers.commit()
                self.cur_players.execute("select count(*) from teams")
                carr=self.cur_players.fetchone()
                new_count=carr[0]
                if new_count==count+1:
                    self.widget_5.show()
                    self.widget.setEnabled(False)
                    self.widget_2.setEnabled(False)
                    self.menubar.setEnabled(False)
                    self.reset_everything()
                else:
                    error_dialog(self,"open","Sorry! Something Went Wrong..")
    elif act=="close":
        self.widget_5.hide()
        self.widget.setEnabled(True)
        self.widget_2.setEnabled(True)
        self.menubar.setEnabled(True)
        self.reset_everything()

def error_dialog(self,act,text="oolala"):
    if act=="open":
        self.widget_6.show()
        self.widget.setEnabled(False)
        self.widget_2.setEnabled(False)
        self.menubar.setEnabled(False)
        self.label_24.setText(text)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
    elif act=="close":
        self.widget_6.hide()
        self.widget.setEnabled(True)
        self.widget_2.setEnabled(True)
        self.menubar.setEnabled(True)
def myscore_board(self,action):
    if action=="cancel":
        self.widget_8.hide()
    elif action=="save":
        new_match.create_match(self)
