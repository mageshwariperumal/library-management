print("**************************************************************************")
print("\t\t\t libray management system \t\t\t")
print("**************************************************************************")
a=input("Enter the name of the vistor:")
b=input("Enter the age of the vistor:")
c=input("Enter the phone no:")
d=input("Enter the address:")
print("**************************************************************************")
print("1.Thriller")
print("2.Fiction")
print("3.Mystery")
print("4.Fantasy")
print("5.Horror")
print("**************************************************************************")
print("name:",a)
print("age:",b)
print("phone no:",c)
print("address:",d)
for i in range(5):
    print(i)
    print("-------------------------------------------------------------")
    wh=int(input("enter the genre type in choice:"))
    if(wh==1):
        print("1.Thriller")
        print("---------------")
        print("1.The guest list")
        print("2.In cold blood")
        print("3.The day of the jackal")
        print("4.Intensity")
        print("---------------")
        w=int(input("if you want to coninue press 1 else press 0.......  :"))
        while(w==1):
            print("-------------------------------------------------------------")
            p=int(input("Enter the book choice you want to know the details:"))
            if(p==1):
                print("book name:The guest list")
                print("Author name:lucy Foley")
                print("overview:A wedding celebration turns dark and deadly in this deliciously wicked and atmospheric thriller reminiscent of Agatha Christie from the New York Times bestselling author of The Hunting Party. On an island off the coast of Ireland, guests gather to celebrate two people joining their lives together as one")
            elif(p==2):
                print("book name:In cold blood")
                print("Auther name:Truman Capote")
                print("overview:Capote learned of the quadruple murder before the killers were captured, and he traveled to Kansas to write about the crime. He was accompanied by his childhood friend and fellow author Harper Lee, and they interviewed residents and investigators assigned to the case and took thousands of pages of notes. Killers Richard Hickock and Perry Smith were arrested six weeks after the murders and later executed by the state of Kansas")
            elif(p==3):
                print("book name:The day of the jackal")
                print("Auther name:Frederick Forsyth")
                print("overview:The Jackal. A tall, blond Englishman with opaque, gray eyes. A killer at the top of his profession. A man unknown to any secret service in the  world. An assassin with a contract to kill the world's most heavily guarded man")
            elif(p==4):
                print("book name:Intensity")
                print("Author name: Dean Koontz")
                print("overview: A murderous sociopath, Edgler Foreman Vess, has entered the house, intent on killing everyone inside. A self-proclaimed “homicidal adventurer,” Vess lives only to satisfy all appetites as they arise, to immerse himself in sensation, to live without fear, remorse, or limits, to live with intensity")
            else:
                print("not option sorry")
            break;
        
    if(wh==2):
        print("2.Fiction")
        print("---------------")
        print("1.Don Quixote")
        print("2.Lord of the Rings")
        print("3.Harry Potter and the Sorcerer's Stone")
        print("4.And Then There Were None")
        print("---------------")
        w=int(input("if you want to coninue press 1 else press 0.......  :"))
        while(w==1):
            p=int(input("Enter the book choice you want to know the details:"))
            if(p==1):
                print("book name:Don Quixote")
                print("Author name:Miguel de Cervantes")
                print("overview:Often referred to as the first modern European novel, Don Quixote follows the exploits of the titular noble who becomes obsessed with the romantic notion of chivalry. On a self-imposed mission to become a knight-errant, Don Quixote recruits common farmer, Sancho Panza, as his squire. Unfortunately, however, their quests rarely end well—among other misadventures, Don Quixote does battle with a herd of sheep, attacks a group of monks, and even frees a group of convicted criminals.")
            elif(p==2):
                print("book name:Lord of the Rings")
                print("Auther name:J.R.R. Tolkien")
                print("overview:This high-fantasy novel is a famous three volume epic. It centers around an all powerful ring forged by the Dark Lord Sauron. For many years the ring is sought after by all likes, but at the start of the novel, it resides in the simple home of the hobbit Bilbo Baggins. Bilbo sets a momentous quest upon his cousin Frodo’s shoulders, tasking him with the journey to Mount Doom to destroy the ring. ")
            elif(p==3):
                print("book name:Harry Potter and the Sorcerer's Stone")
                print("Auther name: J.K. Rowling")
                print("overview:he most recent novel on this list, Harry Potter and the Sorcerer’s Stone brings readers into a world of magic at Hogwarts School of Witchcraft and Wizardry. On his eleventh birthday, Harry’s magical heritage is brought to light by the bumbling half-giant Hagrid. As he embarks on his new life as a wizard, he finds that there’s more to this news than just learning spells and potions. The Dark Lord Voldemort, who had tried and failed to kill Harry as an infant, is regaining power, and Harry stands in his path.")
            elif(p==4):
                print("book name:And Then There Were None")
                print("Author name: Agatha Christie")
                print("overview:From acclaimed mystery author Agatha Christie, And Then There Were None is a mastery of tension. A quirky millionaire hosts a gathering of eight strangers on a private island off of the English coast. When the guests arrive, the elusive host is nowhere to be found. In his place, however, is the accusation of murder upon each of the guests.")
            else:
                print("not option sorry")
            break;
    if(wh==3):
        print("3.Mystery")
        print("---------------")
        print("1.The Big Sleep ")
        print("2. Gone Girl ")
        print("3.Woman in White")
        print("4.Anatomy of a Murder")
        print("---------------")
        w=int(input("if you want to coninue press 1 else press 0.......  :"))
        while(w==1):
            p=int(input("Enter the book choice you want to know the details:"))
            if(p==1):
                print("book name:The Big Sleep ")
                print("Author name:Raymond Chandler")
                print("overview: The Big Sleep is no ordinary story: private eye Philip Marlowe gets hired to investigate the blackmailing of Carmen Sternwood, the second daughter of a wealthy general. The further he digs into this messy business, the more complicated the story gets, as Carmen continues to be blackmailed by others in a web of unexpected relations between the characters. ")
            elif(p==2):
                print("book name: Gone Girl ")
                print("Auther name:Gillian Flynn")
                print("overview: Gone Girl is the ultimate mystery puzzle for the modern media age. Devoted wife Amy’s sudden disappearance throws Nick Dunne into a hailstorm of suspicion — from her parents to his neighbours to the investigators, everyone leans towards believing that he is somehow responsible. Nick himself becomes aware of how his wife viewed him, as well as how little he knows of her, when stories of her emerge from friends he’s never heard of")
            elif(p==3):
                print("book name:Woman in White")
                print("Auther name: Wilkie Collins")
                print("overview:  It follows what first appears to be a simple story of two star-crossed lovers — Walter Hartright and Laura Fairlie — who weren’t meant to be together. Laura was betrothed to Sir Percival Glyde and yet she was mysteriously warned not to proceed with the marriage. Meanwhile, the city is gripped by the story of a strange woman clad in white who’s roaming its dark street.")
            elif(p==4):
                print("book name:Anatomy of a Murder")
                print("Author name: Robert Traver")
                print("overview:It follows lawyer Paul Biegler and his defense of Frederick Manion, who’s accused of murdering an innkeeper. While the case is overwhelmingly against Manion, his unreliable behavior leaves room for challenges against conviction, and that’s where Biegler and his seemingly laid-back attitude comes in. This thrilling courtroom drama will keep you on the edge of your seat, wondering how this lawyer can argue such an impossible case. ")
            else:
                print("not option sorry")
            break;
    if(wh==4):
        print("4.Fantasy")
        print("---------------")
        print("1.GAME OF THRONES ")
        print("2.THE NAME OF THE WIND")
        print("3.THE WAY OF KINGS ")
        print("4.AMERICAN GODS ")
        print("---------------")
        w=int(input("if you want to coninue press 1 else press 0.......  :"))
        while(w==1):
            p=int(input("Enter the book choice you want to know the details:"))
            if(p==1):
                print("book name:GAME OF THRONES ")
                print("Author name:GEORGE R.R. MARTIN")
                print("overview: This novel launched the Song of Ice and Fire series and upended the established tropes of 1990s-era epic fantasy. Let’s not forget that shocking death at the end! I know it’s hard to believe now, but back then, that was something of a fantasy no-no. ")
            elif(p==2):
                print("book name: THE NAME OF THE WIND")
                print("Auther name: PATRICK ROTHFUSS")
                print("overview:While good writing certainly permeates the fantasy genre, it’s not necessarily a requirement. Above all, we want a good story and as long as the prose is readable, that’s fine. Rothfuss’s debut novel showed us that an epic fantasy novel could feature not only good writing, it could showcase beautiful prose. But what’s most interesting about The Name of the Wind is its structure. We first meet Kvothe when he’s a broken man, after the battle has been fought. The mystery of how he got to that end point from his beginnings as an audacious prodigy is part of the series’s charm.")
            elif(p==3):
                print("book name:THE WAY OF KINGS ")
                print("Auther name: BRANDON SANDERSON")
                print("overview:Sanderson is arguably one of the most prolific fantasy writers working in the genre today. In a genre where readers are used to waiting years between series installments, that’s very refreshing. I can’t overstate this fact. It’s one of the reasons he’s gathered a very large, dedicated fanbase. If you’re not familiar with Sanderson’s work, he’s best known for his clearly delineated, almost scientifically laid out magic systems.")
            elif(p==4):
                print("book name:AMERICAN GODS ")
                print("Author name:NEIL GAIMAN")
                print("overview:While Gaiman’s short stories are my personal favorites of his writings, most fiction readers meet him through his novels. American Gods reimagines myths and gods in the modern age, mashes them up with Americana, and takes you on a road trip. I can see why this is one of his most famous works")
            else:
                print("not option sorry")
            break;
    if(wh==5):
        print("5.Horror")
        print("---------------")
        print("1.NINETEEN EIGHTY-FOUR")
        print("2.NIGHT")
        print("3.THE HAUNTING OF HILL HOUSE ")
        print("4.BURNT OFFERINGS ")
        print("---------------")
        w=int(input("if you want to coninue press 1 else press 0.......  :"))
        while(w==1):
            p=int(input("Enter the book choice you want to know the details:"))
            if(p==1):
                print("book name:NINETEEN EIGHTY-FOUR")
                print("Author name:GEORGE ORWELL")
                print("overview:Obviously, no list of the scariest books of all time would be complete without the quintessential dystopian novel. George Orwell’s classic tale of fascist England — now known as Airstrip One — centers on Winston: a propagandist by day and thought-criminal by night. Nineteen Eighty-Four has become a cultural touchstone in the 70-plus years since its release. The fact that it remains relevant today, in our contemporary age of surveillance and militarism, earns it a place on this list.")
            elif(p==2):
                print("book name:NIGHT")
                print("Auther name:ELIE WIESEL")
                print("overview:Let me preface this by saying that, thanks to a cognate in history and comparative religion, I took whole courses on the Third Reich in college. My professors never shied away from the abject horrors of Nazism. Yet nothing prepared me for some of the scenes in this book. Nobel laureate Elie Wiesel draws on his firsthand experiences at Auschwitz and Buchenwald in this brief book, the first in a trilogy about the impact of the Holocaust.")
            elif(p==3):
                print("book name:THE HAUNTING OF HILL HOUSE")
                print("Auther name:SHIRLEY JACKSON")
                print("overview:When it comes to haunted-house stories, it’s hard to beat this Shirley Jackson classic. The Haunting of Hill House follows a paranormal investigator and his two new assistants into the titular manor house. Accompanied by Hill House’s future owner, they begin a doomed expedition, exploring and documenting their ever-unsettling journey through the residence’s weird architecture. As the central characters confront strange phenomena, they’re left to wonder whether Hill House is truly haunted…or if it’s all in their heads.")
            elif(p==4):
                print("book name:BURNT OFFERINGS ")
                print("Author name:ROBERT MARASCO ")
                print("overview:Set in a magnificent, coastal vacation home in the middle of summer, this novel is the other side of The Shining‘s wintry, landlocked coin. The story here centers on the Rolfes: a family of city-dwellers looking for a peaceful summer getaway. What they find, however, is anything but.")
            else:
                print("not option sorry")
            break;
