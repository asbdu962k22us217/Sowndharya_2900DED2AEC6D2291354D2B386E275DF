class player:
  def play(self):
    print("the player is playing cricket")
class betsman(player):
   def play(self):
     print("the betsman is batting")
class bowler(player):
   def play(self):
       print("the bowler is bowling")
betsman=betsman()
bowler=bowler()
betsman.play()
bowler.play()