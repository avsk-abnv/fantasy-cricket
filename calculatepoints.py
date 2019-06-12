from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3,json,random,math,dialogs,new_match
def calculate_points(self):
    self.cur_players.execute("select played_by from match_played where match_id like ?;",(self.comboBox.currentText(),))
    get_team=self.cur_players.fetchone()
    if get_team!=None:
        team=get_team[0]
        if team==self.comboBox_2.currentText():
            sql="select * from "+self.comboBox.currentText()+";"
            self.cur_players.execute(sql)
            get_all=self.cur_players.fetchall()
            total_points=0
            for player_score in get_all:
                player_dict={}
                player_dict['name']=player_score[0]
                player_dict['runs']=player_score[1]
                player_dict['balls']=player_score[2]
                player_dict['4']=player_score[3]
                player_dict['6']=player_score[4]
                player_dict['wkts']=player_score[8]
                player_dict['field']=0
                player_dict['field']+=player_score[9]
                player_dict['field']+=player_score[10]
                player_dict['field']+=player_score[11]
                player_dict['bowled']=player_score[5]
                player_dict['overs']=player_score[5]/6
                points=get_points(self,player_dict)
                new_match.correction(self)
                for i in range(self.listWidget_3.count()):
                    if player_dict['name']==self.listWidget_3.item(i).text():
                        self.listWidget_4.item(i).setText(str(points))
                total_points+=points
            self.label_21.setText(str(total_points))
        else:
            dialogs.error_dialog(self,"open",self.comboBox.currentText()+" is not played by team "+self.comboBox_2.currentText())
    else:
        dialogs.error_dialog(self,"open","Select the Match !")

def get_points(self,player):
    points=0
    #--------------Batting----------------
    if player.get('runs')>0:
        #For every 2 runs
        points+=math.floor(player.get('runs')/2)
        #For century
        if(player.get('runs')>=100):
            points+=10
        #For each half century
        if(player.get('runs')>=50):
            points+=5
        #Strike rate points
        strike_rate=100*player.get('runs')/player.get('balls')
        if (strike_rate>=80 and strike_rate<=100):
            points+=2
        elif (strike_rate>100):
            points+=4
        #For fours & sixes
        points+=2*player.get('6')
        points+=player.get('4')
    #--------------Bowling-------------
    if player.get('bowled')>0:
        #For each wicket
        points+=10*player.get('wkts')
        #3 Wickets per innings
        points+=5*math.floor(player.get('wkts')/3)
        #5 or more wickets
        if (player.get('wkts')>=5):
            points+=10
        #Economy rate
        economy_rate=player.get('runs')/player.get('overs')
        if (economy_rate>=3.5 and economy_rate<4.5):
            points+=4
        elif (economy_rate<3.5 and economy_rate>=2):
            points+=7
        elif (economy_rate<2):
            points+=10
    #For fielding
    points+=10*player.get('field')
    return points
