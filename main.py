from sys import exit
health = 10
def Fire_room():
    print("Oh lord! Everything is on fire! The Fire Suit is over across the gap!")

    choice = input("> ")
    if "shot" in choice:
        print("You are pulled to the other side by the Hookshot.")
        print("You are now immune to fire.")
        print("You see a Great Dodongo, what do you do? Wait use those bombs!")
        choice = input("> ")
        if "bomb" in choice:
          
          print("The Dodongo ate the bomb! Yes!")
          print("You find a pack of bombs and a triforce shard!")
          print("Type the command 'bomb' to use bombs.")
          print("Wait, your sword is glowing!")
          print("The shards of the Triforce are fusing!")
          print("You got the Triforce of Courage!")
          print("You got the Master Sword! Type 'mattack' to use it!")
          print("You sense an evil presence in the next room.")
          choice = input("> ")
          if "room" in choice:
            ganon_room()
    else:
      dead("You burn alive in the inferno!")
def Water_room():
    print("This room is filled with water but there is a switch on the other side, what do you do?")

    choice = input("> ")
    if "boomerang" in choice:
        print("you manage to just hit the switch with your Better Boomerang.")
        print("A bridge appears!")
        choice = input("> ")
        if "cross" in choice:
          
          print("You find a Triforce Shard behind the switch!")
          print("You find a Hookshot!")
          print("Type the command 'shot' to use it.")
          print("Another room!")
          choice = input("> ")
          if "room" in choice:
            Fire_room()
    elif "rang" in choice:
        print("You see that your Boomerang has not enough range to hit the switch.")
    elif "leave" in choice:
      print("Nope I'm out")
      Skull_room
    else:
      print("This is confusing, maybe use a ranged option?")
def ganon_room():
    print("This room has a very Angry Ganon.  What do you do?")

    choice = input("> ")
    if "mattack" in choice:
        print("Nice, you got him, he's dead!")
        print("Princess Zelda descends from a crystal in the ceiling and Ganon drops the Infinity Gaunlet")
        print("Use the command 'snap' to use it, or 'Zelda' to rescue Zelda, or just dance.")
        choice = input("> ")
        if "snap" in choice:
          print("You grin wickedly as you snap your fingers, using the Triforce as extra fuel, you kill literally everyone except you and Zelda.")
          seal("Zelda then uses her sealing powers to seal you.")
        elif "Zelda" in choice:
          print("You use the Hookshot to go home with Zelda.")
          Zhome_room()
        elif "dance" in choice:
          Dance_room()
        else:
          print("You do your last HMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM before going home with Zelda.")
          Zhome_room()
    else:
        dead("He stands there and suddenly you body gets turned inside out and yeeted out the window.")


def house_room():
    print("There is a chest here.")
    print("There is also a bed")
    print("You can open the chest, look under the bed, sleep in the bed, or leave.")
    print("What to do?")

    while True:
        choice = input("> ")

        if "chest" in choice:
            print("You look in the chest and take the Kokiri Sword.")
            print("Use the sword with the command 'attack'.")
        elif "under" in choice :
            print("You look under the bed to take a boomerang.")
            print("You can use it with the command 'rang'.")
        elif "sleep" in choice:
            print("You slept a full 10 hours, so all your health is back!")
            health = 10
        elif "leave" in choice:
            start()
        else:
            print("hmmmmmmmmmmmm.")

def Dance_room():
  print("You can dance for eternity.")
  print("Destroy the room with a bomb to go home.")
    

  choice = input("> ")
   
  if "bomb" in choice:
    house_room
  else:
    print("Dance forever to this tune..."
  "Hey!"
"We are number one, hey!"
"We are number one"
"Now, listen closely "

"Here is a little lesson in trickery "
"This is going down in history "
"If you wanna be a villain number one "
"You have to chase a superhero on the run "

"Just follow my moves and sneak around "
"Be careful not to make a sound, shh "
"No! Do not touch that! "

'We are number one, hey! '
"We are number one "
"We are number one "

"Ha, ha, ha! Now, look at this net that I just found "
"When I say: Go, be ready to throw. Go! "
"Throw it at him, not me! "
"Oh! Let us try something else "

"Now watch and learn, here is the deal "
"He will slip and slide on this banana peel, ha, ha, ha! "
"What are you doing?! "

"Hey! "

"Ba, ba-biddly-ba, ba-ba-ba "
"Ba-ba-ba-ba-ba, ba-ba, we are number one, hey! "
"Ba, ba-biddly-ba, ba-ba-ba "
"Ba-ba-ba-ba-ba, ba-ba "
"Villain number one!"

"Hey!"

"Hey! Ba, ba-biddly-ba, ba-ba-ba "
"Ba-ba-ba-ba-ba, ba-ba, we are number one, hey! "
"Ba, ba-biddly-ba, ba-ba-ba "
"Ba-ba-ba-ba-ba, ba-ba ?"

"We are number one "
"We are number one "
"We are number one, hey, hey! ")

def Skull_room():
    print("Here you see the great evil Skultula.")
    print("He, it, whatever stares at you and you stare back petrified.")
    print("What do you do? Attack it? Leave? Something Else?")

    choice = input("> ")

    if "rang" in choice:
        print("You find that the Skulltula is stunned.")
        print("You walk past it with ease.")
        print("You claim the Triforce Shard from it's chest.")
        print("You also find a Better Boomerang in it's other chest.")
        print("Use 'boomerang' to use it.")
        print("Oooo, another room!")
        choice = input("> ")
        if "go" in choice:
          {
          Water_room()
          }
    elif "attack" in choice:
        print("You find that it is immune to your blow.")
        dead("It eats you whole, weapon and all.")
    else:
        print("The spider uses it's thorax to butt you out of the room.")
        start()


def dead(why):
    print(why, "Good job! Welcome to the after life!")
    exit(0)
def seal(why):
    print(why, "Good Job! Have fun in the sacred realm!")
    exit(0)

def start():
    print("You are at the foot of Ganon's Castle.")
    print("You can go back home or you can go in the castle.")
    print("Where do you go?")

    choice = input("> ")

    if "home" in choice:
        house_room()
    elif "castle" in choice:
        Skull_room()
    else:
        print("You camp for a while.")
        start()

def Zhome_room():
  print("You finally get home with Zelda, but something seems off, like a new presence has appeared under your home, wait, a trapdoor?")
  print("Do you enter the trapdoor?")
  choice = input("> ")
  
  if "yes" in choice:
    funny_room()
  else:
    print("Eh probably nothing, let's just relax with our new legend status.")
    exit(0)


def funny_room():
  print("You look under the trapdoor in your house to find a staircase. ")
  print("You descend the staircase to find a simple puzzle.")
  print("What is the artifact your greatest enemy drops?")
  choice = input("Your Answer? > ")

  if "infinity gauntlet" in choice:
    print("You manage to unlock the door with your answer, and you feel your heroics crawling on you back in the dank hallway.")
    print("You see a small figure lurking in the corner, as if his animations weren't complete, he was T-posing.")
    print("When your eyes finally adjust to the darkness, you see a live skeleton in a blue jacket, T-posing.")
    print("The Skeleton says, 'Hey, where am I? This isn't where I...' He cuts off, and he simply stands there.")
    print("The Skeleton continues, and asks for you to shake his hand.")
    print("Do you accept?")
    choice = input("> ")

    if "yes" in choice:
      print("As you grasp the finger bones there is a loud noise as the skeleton laughs.")
      print("He Says, 'Heh, old whoopie cushion in the hand trick, always funny, anyway, I'll see you in another timeline!")
      print("I'm going back to my game, Undertale!")
      print("You say, 'alright I'm done let's just go to Zelda and fix the mess Ganon made.'")
      exit(0)

    elif "no" in choice:
      print("He smacks your hand and says,'c'mon buddy, be nice!'")
      print("The Skeleton says, 'I'm taking you back to my game, Undertale.'")
      dead("You die in the process of going to Undertale, hearing the Skeleton say, 'get dunked on'.")
start()
