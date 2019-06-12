from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3,json,random,math,dialogs
def play_thematch(self,act):
    self.fill_thelist()
    if self.comboBox.currentText()=="+ Play a New Match":
        if act=="showButton":
            self.playTheMatch.show()
        elif act=="play":
            team=self.comboBox_2.currentText()
            #print(team)
            self.cur_players.execute("select players from teams where name like ?;",(team,))
            players=self.cur_players.fetchone()
            player_list=json.loads(players[0])
            batting_lineup=[]
            bowlers_for_batting=[]
            batsman_for_batting=[]
            batting_value=[]
            player_val={}
            player_ctg={}
            for player in player_list:
                self.cur_players.execute("select value,ctg from stats where player like ?;",(player,))
                rec=self.cur_players.fetchone()
                player_val[player]=rec[0]
                player_ctg[player]=rec[1]
                if player_ctg[player]=="BAT" or player_ctg[player]=="AR" or player_ctg[player]=="WK":
                    batting_value.append(player_val[player])
                    batsman_for_batting.append(player)
                else:
                    bowlers_for_batting.append(player)
            random.shuffle(bowlers_for_batting,random.random)
            batting_value.sort()
            batting_value.reverse()
            start=0
            last_batsman=""
            for value in batting_value:
                for batsman in batsman_for_batting:
                    if player_val[batsman]==value and batsman!=last_batsman:
                        batting_lineup.append(batsman)
                        last_batsman=batsman
                        break
            for player in bowlers_for_batting:
                batting_lineup.append(player)
            i=0
            scoreboard=[]
            total_runs=0
            for player in batting_lineup:
                score=match_score(self,player,player_ctg[player],player_val[player],i)
                scoreboard.append(score)
                total_runs+=score[1]
                i=i+1

            if self.player_batted<11:
                total_ballsfaced=300
                ballfaced_tillnow=0
                for score in scoreboard:
                    plusminus=random.randint(0,2*int(score[1]*0.35))-int(score[1]*0.35)
                    score[2]=score[1]+plusminus
                    #print(score[2])
                    ballfaced_tillnow+=score[2]
                #print("---------------------")
                new_exballs=0
                if ballfaced_tillnow!=total_ballsfaced:
                    extra_balls=ballfaced_tillnow-total_ballsfaced
                    for score in scoreboard:
                        score[2]-=int(extra_balls*score[1]/total_runs)
                        #balls=score[2]-int(extra_balls*score[1]/total_runs)
                        #print(score[2])
                        new_exballs+=score[2]
                    #print("----------------------")
                    if new_exballs!=total_ballsfaced:
                        max_score=0
                        for score in scoreboard:
                            if score[2]>=max_score:
                                max_score=score[2]
                        for score in scoreboard:
                            if score[2]==max_score:
                    #            score[2]-=new_exballs-total_ballsfaced
                                balls=score[2]-(new_exballs-total_ballsfaced)
                                score[2]=balls
                                #print(score[2])
            else:
                total_ballsfaced=random.randint(200,300)
                ballfaced_tillnow=0
                for score in scoreboard:
                    plusminus=random.randint(0,2*int(score[1]*0.35))-int(score[1]*0.35)
                    score[2]=score[1]+plusminus
                    #print(score[2])
                    ballfaced_tillnow+=score[2]
                #print("---------------------")
                new_exballs=0
                if ballfaced_tillnow!=total_ballsfaced:
                    extra_balls=ballfaced_tillnow-total_ballsfaced
                    for score in scoreboard:
                        score[2]-=int(extra_balls*score[1]/total_runs)
                        #balls=score[2]-int(extra_balls*score[1]/total_runs)
                        #print(score[2])
                        new_exballs+=score[2]
                    #print("----------------------")
                    if new_exballs!=total_ballsfaced:
                        max_score=0
                        for score in scoreboard:
                            if score[2]>=max_score:
                                max_score=score[2]
                        for score in scoreboard:
                            if score[2]==max_score:
                    #            score[2]-=new_exballs-total_ballsfaced
                                balls=score[2]-(new_exballs-total_ballsfaced)
                                score[2]=balls
            bll=random.randint(30,60)
            bowled_5=[bll,48,60,56,60]
            bowled_6=[60,60,bll,42,48,30]
            bowled_7=bowled_6
            bowled_7.append(0)
            random.shuffle(bowled_5,random.random)
            random.shuffle(bowled_6,random.random)
            random.shuffle(bowled_7,random.random)
            i=0
            bowlers=[]
            all_rounders=[]
            if len(bowlers_for_batting)<5:
                for bowler in bowlers_for_batting:
                    bowlers.append(bowler)
                for player in player_list:
                    if player_ctg[player]=="AR":
                        all_rounders.append(player)
                for i in range(5-len(bowlers_for_batting)):
                    bowlers.append(all_rounders[i])
            else:
                bowlers=bowlers_for_batting
            for bowler in bowlers:
                for score in scoreboard:
                    if bowler==score[0]:
                        if len(bowlers)==5:
                            score.append(bowled_5[i])
                            i=i+1
                        elif len(bowlers)==6:
                            score.append(bowled_6[i])
                            i=i+1
                        elif len(bowlers)==7:
                            score.append(bowled_7[i])
                            i=i+1
            maiden=[0,0,1,0,2,0,1]
            given=[]
            for i in range(6):
                given.append(random.randint(20,80))
            wickets=[0,0,0,0,0,0]
            total_wickets=random.randint(0,10)
            for k in range(6):
                wickets[random.randint(0,6)-1]+=1
            i=0
            random.shuffle(maiden,random.random)
            for bowler in bowlers:
                for score in scoreboard:
                    if bowler==score[0] and score[5]!=0:
                        #print("{}--maiden:{},given:{},wickets:{}".format(score[0],maiden[i],given[i],wickets[i]))
                        score.append(maiden[i])
                        score.append(given[i])
                        score.append(wickets[i])
                        #print(score)
                        i=i+1
                        break
                    elif bowler==score[0] and score[5]==0:
                        score.append(0)
                        score.append(0)
                        score.append(0)
                        break
            flag=False
            for player in player_list:
                flag=False
                for bowler in bowlers:
                    if player==bowler:
                        flag=True
                        break
                if flag==False:
                    for score in scoreboard:
                        if player==score[0]:
                            score.append(0)
                            score.append(0)
                            score.append(0)
                            score.append(0)
                            break
            max_wicksleft=10-total_wickets
            total_wicks=random.randint(1,max_wicksleft)-1
            total_catches=0
            total_stumps=0
            total_ro=0
            for i in range(total_wicks):
                type_wkt=random.randint(1,3)
                if type_wkt==1:
                    total_catches+=1
                elif type_wkt==2:
                    total_stumps+=1
                elif type_wkt==3:
                    total_ro+=1
            for score in scoreboard:
                score.append(0)
            catch_index=len(scoreboard[1])-1
            for i in range(total_catches):
                lucky_catch=random.randint(0,11)-1
                scoreboard[lucky_catch][catch_index]+=1
            for score in scoreboard:
                score.append(0)
            stump_index=len(scoreboard[1])-1
            wkt_keeper=""
            for player in player_list:
                if player_ctg[player]=="WK":
                    wkt_keeper=player
                    break
            for score in scoreboard:
                if score[0]==wkt_keeper:
                    score[stump_index]=total_stumps
            for score in scoreboard:
                score.append(0)
            ro_index=len(scoreboard[1])-1
            for i in range(total_ro):
                lucky_ro=random.randint(0,11)-1
                scoreboard[lucky_ro][ro_index]+=1

            #for score in scoreboard:
            #    print(score)
            playedby=self.comboBox_2.currentText()
            setme=""
            for i in range(11):
                for j in range(12):
                    if j==0:
                        if scoreboard[i][0].find(' ')>0:
                            setme=scoreboard[i][0][0]+". "+scoreboard[i][0][scoreboard[i][0].index(' ')+1:]
                    else:
                        setme=str(scoreboard[i][j])
                    self.scoretext[i][j].setText(setme)
                    self.scoretext[i][j].setAlignment(QtCore.Qt.AlignCenter)
            self.widget_8.show()
            self.score_board=scoreboard
            self.playedby_=playedby
            #self.create_match(scoreboard,playedby)
            self.label_31.setText(playedby)
            self.cur_players.execute("select count(*) from match_played")
            get_count=self.cur_players.fetchone()
            count=get_count[0]+1
            match_id="Match_"+str(count)
            self.label_29.setText(match_id)
    else:
        self.playTheMatch.hide()
        self.cur_players.execute("select played_by from match_played where match_id like ?;",(self.comboBox.currentText(),))
        cnf=self.cur_players.fetchone()
        confirmation=False
        if cnf[0]==self.comboBox_2.currentText():
            confirmation=True
        if confirmation==True:
            correction(self)
        else:
            dialogs.error_dialog(self,"open",self.comboBox.currentText()+" is not played by team "+self.comboBox_2.currentText())


def match_score(self,player,ctg,val,select):
    if select==0:
        self.player_batted=random.randint(3,11)
        get_triplets=getruns_sixesfours(self,ctg,val)
        runs=get_triplets[0]
        sixes=get_triplets[1]
        fours=get_triplets[2]
    else:
        if select<self.player_batted:
            get_triplets=getruns_sixesfours(self,ctg,val)
            runs=get_triplets[0]
            sixes=get_triplets[1]
            fours=get_triplets[2]
        else:
            runs=0
            sixes=0
            fours=0
    return [player,runs,0,fours,sixes]

def getruns_sixesfours(self,ctg,val):
    if ctg=="BAT" or ctg=="AR" or ctg=="WK":
        if val>80:
            prob=random.randint(0,10)
            if prob<9:
                runs=random.randint(49,99)
            elif prob==9:
                runs=random.randint(100,200)
            elif prob==10:
                runs=random.randint(10,50)
        elif val<80 and val>=60:
            prob=random.randint(0,20)
            if prob<10:
                runs=random.randint(49,99)
            elif prob==20:
                runs=random.randint(100,150)
            elif prob>=10 and prob<20:
                runs=random.randint(0,50)
        elif val<60 and val>=40:
            prob=random.randint(0,20)
            if prob<8:
                runs=random.randint(49,99)
            elif prob==20:
                runs=random.randint(100,150)
            elif prob>=8 and prob<20:
                runs=random.randint(0,50)
        elif val<40:
            prob=random.randint(0,10)
            if prob==10:
                runs=random.randint(40,100)
            elif prob==8 or prob==9:
                runs=random.randint(25,40)
            elif prob<8:
                runs=random.randint(0,25)
    else:
        runs=random.randint(0,30)
    sixes=int(runs*0.1*random.randint(0,5)/6)
    fours=int(runs*0.1*random.randint(0,5)/4)
    return [runs,sixes,fours]
def create_scoretext(self):
    self.scoretext=[]
    for i in range(11):
        self.scoretext.append([])
        for j in range(12):
            score = QtWidgets.QLabel(self.widget_8)
            self.scoretext[i].append(score)
    top=80
    left_0=11
    for i in range(11):
        left=100
        top+=34
        for j in range(12):
            if(j==0):
                self.scoretext[i][j].setGeometry(QtCore.QRect(left_0, top, 80, 13))
                self.scoretext[i][j].setStyleSheet("border:none;\n"
        "color: gold;")
            else:
                self.scoretext[i][j].setGeometry(QtCore.QRect(left, top, 40, 13))
                left+=48
                self.scoretext[i][j].setStyleSheet("border:none;\n"
        "color: white;")
            objstr="scoretext_"+str(i)+"_"+str(j)
            self.scoretext[i][j].setObjectName(objstr)
def correction(self):
    sql_="select player from "+self.comboBox.currentText()
    self.cur_players.execute(sql_)
    match_players=self.cur_players.fetchall()
    self.cur_players.execute("select players from teams where name like ?;",(self.comboBox_2.currentText(),))
    _playersget_=self.cur_players.fetchone()
    teams_players=json.loads(_playersget_[0])
    #self.listWidget_3.clear()
    players_not_played=[]
    for _player_ in teams_players:
        played_or_not=False
        for player_ in match_players:
            if _player_==player_[0]:
                played_or_not=True
                break
        if played_or_not==False:
            players_not_played.append(_player_)
    tobeadded=[]
    players_who_played=[]
    for player_ in match_players:
        played_or_not=True
        for _player_ in teams_players:
            if _player_==player_[0]:
                played_or_not=False
                break
        if played_or_not==True:
            players_who_played.append(player_[0])
    if len(players_not_played)>0 and len(players_who_played)>0:
        for i in range(self.listWidget_3.count()):
            k=0
            for player in players_not_played:
                if self.listWidget_3.item(i).text()==player:
                    self.listWidget_3.item(i).setText(players_who_played[k])
                    k+=1
def create_match(self):
    scoreboard=self.score_board
    playedby=self.playedby_
    #self.label_31.setText(playedby)
    self.cur_players.execute("select count(*) from match_played")
    get_count=self.cur_players.fetchone()
    count=get_count[0]+1
    match_id="Match_"+str(count)
    #self.label_29.setText(match_id)
    self.cur_players.execute("insert into match_played (match_id,played_by) values (?,?);",(match_id,playedby))
    self.cur_players.execute("select count(*) from match_played")
    get_count_new=self.cur_players.fetchone()
    confirmation=False
    if get_count_new>get_count:
        confirmation=True
    if confirmation==True:
        sql='''CREATE TABLE '''+match_id+''' (
                                    Player   CHAR (50) PRIMARY KEY,
                                    Scored   INT (5)   NOT NULL,
                                    Faced    INT (5)   NOT NULL,
                                    Fours    INT (5)   NOT NULL,
                                    Sixes    INT (5)   NOT NULL,
                                    Bowled   INT (5)   NOT NULL,
                                    Maiden   INT (5)   NOT NULL,
                                    Given    INT (5)   NOT NULL,
                                    Wkts     INT (5)   NOT NULL,
                                    Catches  INT (5)   NOT NULL,
                                    Stumping INT (5)   NOT NULL,
                                    R_out    INT (5)   NOT NULL
                                );'''
        self.cur_players.execute(sql)
        self.myplayers.commit()
        #print(sql)
        for score in scoreboard:
            sql="insert into "+match_id+" (Player,Scored,Faced,Fours,Sixes,Bowled,Maiden,Given,Wkts,Catches,Stumping,R_out) values ("
            i=0
            for score_single in score:
                if i==0:
                    sql+="'"+str(score_single)+"',"
                else:
                    sql+=str(score_single)+","
                i=i+1
            sql=sql[:-1]
            sql+=");"
            #print(sql)
            self.cur_players.execute(sql)
        self.myplayers.commit()
        self.widget_8.hide()
        self.widget_5.show()
        self.label_22.setText("Match has been saved Successfully !")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)                    
