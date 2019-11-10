from tkinter import*
from math import*



def piece(x1,y1,bn):
    global mat
    
    canvas.create_rectangle(x1*40+5,y1*40+5,x1*40+44,y1*40+44,fill=bn,outline=bn)
    recup = mat[y1][x1]
    if recup-20>0:
        blgo = "gold"
    else:
        blgo = "blue"
    
    if recup == 11 or recup == 21:
        if blgo == "gold":
            canvas.create_image(x1*40+25,y1*40-2,image=images[0])
        else:
            canvas.create_image(x1*40+25,y1*40-1,image=images[6])    
    elif recup == 12 or recup == 22:
        if blgo == "gold":
            canvas.create_image(x1*40+25,y1*40+15,image=images[1])
        else:
            canvas.create_image(x1*40+25,y1*40+15,image=images[7])
    elif recup == 13 or recup == 23:
        if blgo == "gold":
            canvas.create_image(x1*40+25,y1*40+15,image=images[2])
        else:
            canvas.create_image(x1*40+25,y1*40+15,image=images[8])
    elif recup == 14 or recup == 24:
        if blgo == "gold":
            canvas.create_image(x1*40+25,y1*40+15,image=images[3])
        else:
            canvas.create_image(x1*40+25,y1*40+15,image=images[9])
    elif recup == 15 or recup == 25:
        if blgo == "gold":
            canvas.create_image(x1*40+25,y1*40+9,image=images[4])
        else:
            canvas.create_image(x1*40+25,y1*40+9,image=images[10])
    elif recup == 16 or recup == 26:
        if blgo == "gold":
            canvas.create_image(x1*40+25,y1*40+11,image=images[5])
        else:
            canvas.create_image(x1*40+25,y1*40+9,image=images[11])
        
        

def souris(event):
    global x,y,ent

    xclic = int(round((event.x-25)/40))
    yclic = int(round((event.y-25)/40))
    if xclic<= 7 and xclic >= 0 and yclic<= 7 and yclic >= 0:
        x = xclic
        y = yclic
        ent = 1



def var():
    global mat,x,y,sx,sy,ent,xsel,ysel,tour, moveroi, lmemoire, numero_tour, xroin,yroin,xroib,yroib, images
    mat = [[16,15,14,13,12,14,15,16],[11,11,11,11,11,11,11,11],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[21,21,21,21,21,21,21,21],[26,25,24,23,22,24,25,26]]
    x=0
    y=0
    sx=0
    sy=0
    ent=0
    xsel=-1
    ysel=0
    xroin = 4
    yroin = 0
    xroib = 4
    yroib = 7
    tour = "blanc"
    moveroi = 0
    numero_tour = 0
    lmemoire = []
    # Chemin d'acces aux dossier des images des pieces a définir :
    chemin = '../images/'

    Nomimage = ['pionb','roib','reineb','foub','cavalierb','tourb','pionn','roin','reinen','foun','cavaliern','tourn']
    images = []
    for a in Nomimage:
        if a in ['roib','reineb','foub','roin','reinen','foun']:
            images.append(PhotoImage(file = chemin + a +".png").subsample(3,6))
        elif a in ['cavalierb','tourb','cavaliern','tourn']:
            images.append(PhotoImage(file = chemin + a +".png").subsample(3,5))
        else:
            images.append(PhotoImage(file = chemin + a +".png").subsample(3,4))
    
    canvas.bind_all('<q>', quitter)
    
    canvas.bind_all('<u>', undo)
    canvas.bind_all('<i>', dodo)
   
    canvas.bind_all('<Button-1>', souris)

   
    
def selectpiece():
    global x, y, sx, sy, ent, xsel, ysel,xroib,yroib,xroin,yroin
    
    if xsel != -1:
        piece(xsel,ysel,"orange")
    if chess(xroib,yroib,10) != []:
        piece(xroib,yroib,"red")
    if chess(xroin,yroin,20) != []:
        piece(xroin,yroin,"red")
    if ent !=1:
        tk.after(50,selectpiece)
    else:
        depl()
    
    
    
def depl():
    global x,y,xsel,ysel, ent, mat, tour, moveroi, val, lmemoire, numero_tour, xroin,yroin,xroib,yroib
    if xsel ==-1:
        if mat[y][x] != 0:
            if ( tour == "blanc" and mat[y][x] > 20 ) or ( tour == "noir" and mat[y][x] < 20):
                xsel=x
                ysel=y
        ent = 0
        selectpiece()
    elif x == xsel and y == ysel:
        norb(x,y)
        xsel=-1
        ysel=0
        ent = 0
        selectpiece()
    elif (mat[ysel][xsel]-20)*(mat[y][x]-20)>0 and mat[y][x]!=0:
        norb(xsel,ysel)
        xsel= x
        ysel=y
        ent = 0
        selectpiece()
    else:
        val = 0
        recup = mat[ysel][xsel]
        if recup == 11 or recup == 21:
            if dpion(x,y,xsel,ysel)==1:
                val = 1
                
        elif recup == 12 or recup == 22:
            val = droi(x,y,xsel,ysel)
            if val==1 or val==2:
                if recup == 22:
                    xroib = x
                    yroib = y
                else:
                    xroin = x
                    yroin = y
        elif recup == 13 or recup == 23:
            if dreinne(x,y,xsel,ysel)==1:
                val = 1
                
        elif recup == 14 or recup == 24:
            if dfou(x,y,xsel,ysel)==1:
                val = 1
                
        elif recup == 15 or recup == 25:
            if dcheval(x,y,xsel,ysel)==1:
                val = 1
                
        elif recup == 16 or recup == 26:
            if dtour(x,y,xsel,ysel)==1:
                val = 1
        
        if val == 1:
            if len(lmemoire)!=numero_tour:
                chier = len(lmemoire)
                for a in range(chier-numero_tour):
                    del(lmemoire[chier-1-a])
                
            lmemoire.append([y,x,mat[y][x],ysel,xsel,mat[ysel][xsel]])
            mat[y][x]=mat[ysel][xsel]
            mat[ysel][xsel] = 0
            norb(xsel,ysel)
            norb(x,y)
            xsel=-1
            ysel=0
            numero_tour+=1
            affcoup()
            if tour == "noir":
                tour = "blanc"
            else:
                tour = "noir"
        elif val == 2:
            xsel=-1
            ysel=0
            numero_tour+=1
            affcoup()
            if tour == "noir":
                tour = "blanc"
            else:
                tour = "noir"
        
        if tour == "noir":
            if chess(xroib,yroib,10) != []:
                undo('<u>',1)
            elif echec_mat(xroin,yroin,20)==0:
                print("echec et mat")
            elif chess(xroin,yroin,20) != []:
                piece(xroin,yroin,"red")
            norb(xroib,yroib)
        else:
            if chess(xroin,yroin,20) != []:
                undo('<u>',1)
            elif echec_mat(xroib,yroib,10)==0:
                print("echec et mat")
            elif chess(xroib,yroib,10) != []:
                piece(xroib,yroib,"red")
            norb(xroin,yroin)
        ent = 0
        selectpiece()
        
    
    
def dpion(xa,ya,xb,yb):
    global mat
    col = mat[yb][xb]
    ar = mat[ya][xa]
        
    if col==11:
        if xa == xb and ar == 0:
            if ya == yb+1:
                return 1
            elif yb == 1 and ya == 3 and mat[2][xa]==0:
                return 1
            else:
                return 0
        elif (xb==xa+1 or xb==xa-1) and ar- 20 > 0 and ar !=0:
            if ya == yb+1:
                return 1
            else:
                return 0
        else:
            return 0
            
    elif col ==21:
        if xa == xb and ar == 0:
            if ya == yb-1:
                return 1
            elif yb == 6 and ya == 4 and mat[5][xa]==0:
                return 1
            else:
                return 0
        elif (xb==xa+1 or xb==xa-1) and ar-20<0 and ar != 0:
            if ya == yb-1:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0
        


def droi(xa,ya,xb,yb):
    global mat
    col = mat[yb][xb]
    ar = mat[ya][xa]
    if rock(xa,ya,xb,yb)==2:
        return 2
    elif (xb==xa or xb == xa+1 or xb == xa -1) and (yb==ya or yb == ya+1 or yb == ya-1):
        if ar != 0:
            if (col-20)*(ar-20)<0:
                return 1
            else:
                return 0
        else:
            return 1
    else:
        return 0
    
    
    
def dreinne(xa,ya,xb,yb):
    if dtour(xa,ya,xb,yb)==1 or dfou(xa,ya,xb,yb)==1:
        return 1
    else:
        return 0
    
    
    
def dfou(xa,ya,xb,yb):
    global mat
    col = mat[yb][xb]
    ar = mat[ya][xa]
    if abs(xa-xb)==abs(ya-yb) and( (ar-20)*(col-20)<0 or ar == 0):
        if xb < xa:
            dx = 1
        else:
            dx = -1
        if yb < ya:
            dy = 1
        else:
            dy = -1
        test = 0
        xc = xb + dx
        yc = yb + dy
        while xc != xa:
            if mat[yc][xc] != 0:
                test = 1
            xc += dx
            yc += dy
        if test== 0:
            return 1
        else:
            return 0
    else:
        return 0
        
    
    
def dcheval(xa,ya,xb,yb):
    global mat
    col = mat[yb][xb]
    ar = mat[ya][xa]
    if (col-20)*(ar-20)<0 or ar == 0:
        if (abs(xa-xb)==2 and abs(ya-yb)==1) or ((abs(xa-xb)==1 and abs(ya-yb)==2)):
            return 1
        else:
            return 0
    else:
        return 0
    
    
    
def dtour(xa,ya,xb,yb):
    global mat
    if mat[ya][xa]==0 or (mat[ya][xa]-20)*(mat[yb][xb]-20)<0:
        if ya==yb:
            if xb>xa:
                xc = xa
                xa = xb
                xb = xc
            test = 0
            for xc in range(xa-xb-1):
                if mat[ya][xc+xb+1] != 0:
                    test = 1
            if test == 0:
                return 1
            else:
                return 0
        elif xa==xb:
            if yb>ya:
                yc = ya
                ya = yb
                yb = yc
            test = 0
            for yc in range(ya-yb-1):
                if mat[yc+yb+1][xa] != 0:
                    test = 1
            if test == 0:
                return 1
            else:
                return 0
    else:
        return 0
    
    
    
def rock(xa,ya,xb,yb):
    global mat, moveroi
    col = mat[yb][xb]
    ar = mat[ya][xa]
    if col == 12 and moveroi == 0 and ya == 0 and ((xa==6 and mat[0][7]==16) or (mat[0][0]==16 and xa == 2)) and chess(xb,yb,20)==[]:
        if xa == 2:
            if mat[0][1]==0 and mat[0][2]==0 and mat[0][3]== 0 and chess(0,3,20) == []:
                if len(lmemoire)!=numero_tour:
                    chier = len(lmemoire)
                    for a in range(chier-numero_tour):
                        del(lmemoire[chier-1-a])
                lmemoire.append([0,4,12,0,0,16,0,1,0,0,2,0,0,3,0])
                mat[0][0]=0
                mat[0][4]=0
                mat[0][2]=12
                mat[0][3]=16
                reinit()
                return 2
            else:
                return 0
        else:
            if mat[0][5]==0 and mat[0][6]==0 and chess(0,5,20)==[]:
                if len(lmemoire)!=numero_tour:
                    chier = len(lmemoire)
                    for a in range(chier-numero_tour):
                        del(lmemoire[chier-1-a])
                lmemoire.append([0,4,12,0,7,16,0,5,0,0,6,0])
                mat[0][7]=0
                mat[0][4]=0
                mat[0][6]=12
                mat[0][5]=16
                reinit()
                return 2
            else:
                return 0
    elif col == 22 and moveroi == 0 and ya == 7 and ((xa==6 and mat[7][7]==26) or (mat[7][0]==26 and xa == 2)) and chess(xb,yb,10)==[]:
        if xa == 2:
            if mat[7][1]==0 and mat[7][2]==0 and mat[7][3]== 0 and chess(7,3,10)==[]:
                if len(lmemoire)!=numero_tour:
                    chier = len(lmemoire)
                    for a in range(chier-numero_tour):
                        del(lmemoire[chier-1-a])
                lmemoire.append([7,4,22,7,0,26,7,1,0,7,2,0,7,3,0])
                mat[7][0]=0
                mat[7][4]=0
                mat[7][2]=22
                mat[7][3]=26
                reinit()
                return 2
            else:
                return 0
        else:
            if mat[7][5]==0 and mat[7][6]==0 and chess(7,5,10)==[]:
                if len(lmemoire)!=numero_tour:
                    chier = len(lmemoire)
                    for a in range(chier-numero_tour):
                        del(lmemoire[chier-1-a])
                lmemoire.append([7,4,22,7,7,26,7,5,0,7,6,0])
                mat[7][7]=0
                mat[7][4]=0
                mat[7][6]=22
                mat[7][5]=26
                reinit()
                return 2
            else:
                return 0
    else:
        return 0
        
    

def chess(x,y,dlt, bloquer = 'non'): #renvoi les pieces de couleur dlt qui attaquent la cas de coordonnées (x,y)
    global mat, danger
    ld = []
    litest = []
    danger = 0
    
    # attaque d'un pion
    if bloquer == 'non':
        if dlt == 10:
            litest = attaqt1([1,-1],[-1,-1],1,x,y,dlt)
            if litest != []:
                ld.append(litest)
                litest = []
        elif dlt == 20:
            litest = attaqt1([1,-1],[1,1],1,x,y,dlt)
            if litest != []:
                ld.append(litest)
                litest = []
    else: 
        if dlt == 10:
            litest = attaqt1([0],[-1],1,x,y,dlt)
            if litest != []:
                ld.append(litest)
                litest = []
            else:
                if y-2 == 1:
                    if mat[y-2][x]==11:
                        ld.append([x,1,1])

        elif dlt == 20:
            litest = attaqt1([0],[1],1,x,y,dlt)
            if litest != []:
                ld.append(litest)
                litest = []
            else:
                if y+2 == 6:
                    if mat[y+2][x]==11:
                        ld.append([x,6,1])
    
    # attaque d'un cavalier
    litest = attaqt1([1,2,2,1,-1,-2,-2,-1],[-2,-1,1,2,2,1,-1,-2],5,x,y,dlt)
    if litest != []:
        ld.append(litest)
        litest = []
    
    # attaque un autre roi
    litest = attaqt1([0,1,1,1,0,-1,-1,-1],[-1,-1,0,1,1,1,0,-1],2,x,y,dlt)
    if litest != []:
        ld.append(litest)
        litest = []
            
    # attaque d'une tour/reinne 
    litest = attaqt2([0,0,1,-1],[-1,1,0,0],6,x,y,dlt)
    if litest != []:
        ld.append(litest)
        litest = []
    
    # attaque d'un fou/reinne
    litest = attaqt2([1,1,-1,-1],[-1,1,-1,1],4,x,y,dlt)
    if litest != []:
        ld.append(litest)
        litest = []
    
    #renvoie les infos
        
    return ld
    
    

def attaqt1(lx,ly,typ,x,y,dlt):
    global danger, mat
    ch = 0
    for a in range(len(lx)):
        x1 = x+lx[a]
        y1 = y+ly[a]
        if x1 <= 7 and x1 >= 0 and y1 <=7 and y1>=0:
            if mat[y1][x1] == dlt+typ:
                danger+=1
                xs = x1
                ys = y1
                ch = 1
    if ch == 1:
        return [xs,ys,typ]
    else:
        return []

def attaqt2(lx,ly,typ,x,y,dlt):
    global danger, mat
    ls = []
    for a in range(4):
        x1 = x + lx[a]
        y1 = y + ly[a]
        while x1 <= 7 and x1 >= 0 and y1 <=7 and y1>=0 and mat[y1][x1]==0:
            x1 += lx[a]
            y1 += ly[a]
        if x1 <= 7 and x1 >= 0 and y1 <=7 and y1>=0:
            if mat[y1][x1]== dlt+3:
                danger+=1
                ls = [x1,y1,3]
            elif mat[y1][x1]== dlt+typ:
                danger+=1
                ls = [x1,y1,typ]
    return ls



def echec_mat(x,y,dlt):# fonctionnel sauf lorsqu'il s'agit de bloquer les trajectoires des attaquants, ou il ne fonctionne que avec les verticales et les horizontaleset ou il ne prend pas en compte les mouvements des petits pions.
    global mat
    #on suppose qu'il n'y a pas d'issu, puis on les cherche
    sol = 0
    
    if chess(x,y,dlt) != []:
        lrx = [0,1,1,1,0,-1,-1,-1]
        lry = [-1,-1,0,1,1,1,0,-1]
        #on verifie que le roi ne peux pas quitter/manger la menace en se deplacant (semble fontionnel)
        for a in range(8):
            x1 = x+lrx[a]
            y1 = y+lry[a]
            if x1 <= 7 and x1 >= 0 and y1 <=7 and y1>=0:
                recup = mat[y1][x1]
                back = mat[y][x]
                if recup == 0:
                    mat[y1][x1]=(30-dlt)+2
                    mat[y][x]=0
                    if chess(x1,y1,dlt)==[]:
                        sol = 1
                    mat[y1][x1]=0
                    mat[y][x]=(30-dlt)+2
                elif (recup-20)*(back-20) < 0:
                    mat[y1][x1]=(30-dlt)+2
                    mat[y][x]=0
                    if chess(x1,y1,dlt)==[]:
                        sol = 1
                    mat[y1][x1]=recup
                    mat[y][x]=(30-dlt)+2
                    
        #si ce n'est pas le cas, on essaye : 
        if sol == 0:
            #de manger la piece qui nous met en echec avec une autre piece que le roi
            if len(chess(x,y,dlt)) == 1:
                l = chess(x,y,dlt)[0]
                piece = dlt+l[2]
                for a in chess(l[0],l[1],30-dlt):
                    #il faut désormais vérifier si en mangeant cette piece, on ne met pas le roi en echec
                    mat[l[1]][l[0]] = mat[a[1]][a[0]]
                    mat[a[1]][a[0]] = 0
                    if chess(x,y,dlt) == [] and a[2] != 2:
                        sol = 1
                    mat[a[1]][a[0]] = mat[l[1]][l[0]]
                    mat[l[1]][l[0]] = piece
                if sol == 0:
                    #de bloquer l'axe d'attaque de la piece si c'est un fou, une tour ou une dame
                    if x==l[0] or y==l[1] or abs(x-l[0])==abs(y-l[1]):
                        if y<l[1]:
                            lverify = [1,2,3,4,5,6,7]
                        elif y>l[1]:
                            lverify = [-1,-2,-3,-4,-5,-6,-7]
                        else:
                            lverify = [0,0,0,0,0,0,0]
                        if x<l[0]:
                            lverifx = [1,2,3,4,5,6,7]
                        elif x>l[0]:
                            lverifx = [-1,-2,-3,-4,-5,-6,-7]
                        else:
                            lverifx = [0,0,0,0,0,0,0]
                        for a in range(max(abs(l[1]-y)-1,abs(l[0]-x)-1)):
                            for b in chess(x+lverifx[a],y+lverify[a],30-dlt,bloquer='oui'):
                                mat[y+lverify[a]][x+lverifx[a]] = mat[b[1]][b[0]]
                                mat[b[1]][b[0]] = 0
                                if chess(x,y,dlt) == [] and b[2] != 2:
                                    sol = 1
                                mat[b[1]][b[0]] = mat[y+lverify[a]][x+lverifx[a]]
                                mat[y+lverify[a]][x+lverifx[a]] = 0
    else:
        sol = 1
    
    return sol

def undo(event, k=0):
    # permet de revenir un coup en arriere
    global mat, lmemoire, numero_tour, tour, xsel, ysel, xroin,yroin,xroib,yroib
    if numero_tour > 0:
        lc = lmemoire[numero_tour-1]
        if xsel != -1:
            norb(xsel,ysel)
            xsel=-1
            ysel=0
        for a in range(int(len(lc)/3)):
            mat[lc[a*3]][lc[a*3+1]] = lc[a*3+2]
            norb(lc[a*3+1],lc[a*3])
        numero_tour-=1
        
        if len(lc)==6:
            if lc[5] == 22:
                xroib = lc[4]
                yroib = lc[3]
            elif lc[5]==12:
                xroin = lc[4]
                yroin = lc[3]
        elif len(lc)==12 or len(lc)==15:
            if lc[2] == 22:
                l = lookfor(22)
                xroib = l[0]
                yroib = l[1]
            elif lc[2]==12:
                l = lookfor(12)
                xroin = l[0]
                yroin = l[1]
        if tour == "noir":
            tour = "blanc"
        else:
            tour = "noir"
        affcoup()
        if k==1:
            del(lmemoire[-1])
            
                
    
def dodo(event):
    #permet de faire le mouvement inverse du undo
    global mat, lmemoire, numero_tour, tour, xsel, ysel, xroin,yroin,xroib,yroib
    if numero_tour < len(lmemoire):
        lc = lmemoire[numero_tour]
        # permet de déselectionner la piece selectionnée si elle existe
        if xsel != -1:
            norb(xsel,ysel)
            xsel=-1
            ysel=0
            
        # permet de faire le coup suivant si ce n'est pas un roque
        if len(lc) == 6:
            mat[lc[0]][lc[1]] = lc[5]
            norb(lc[1],lc[0])
            mat[lc[3]][lc[4]] = 0
            norb(lc[4],lc[3])
            if lc[5] == 22:
                xroib = lc[1]
                yroib = lc[0]
            elif lc[5]==12:
                xroin = lc[1]
                yroin = lc[0]
        #le reste pour le rock
        elif len(lc)==12:
            if lc[0]==7:
                mat[7][7]=0
                mat[7][4]=0
                mat[7][6]=22
                mat[7][5]=26
                xroib = 6
                yroib = 7
                norb(7,7)
                norb(4,7)
                norb(6,7)
                norb(5,7)
            else:
                mat[0][7]=0
                mat[0][4]=0
                mat[0][6]=12
                mat[0][5]=16
                xroin = 6
                yroin = 0
                norb(7,0)
                norb(4,0)
                norb(6,0)
                norb(5,0)
        elif len(lc)==15:
            if lc[0]==7:
                mat[7][0]=0
                mat[7][4]=0
                mat[7][2]=22
                mat[7][3]=26
                xroib = 2
                yroib = 7
                norb(0,7)
                norb(4,7)
                norb(2,7)
                norb(3,7)
            else:
                mat[0][0]=0
                mat[0][4]=0
                mat[0][2]=12
                mat[0][3]=16
                xroin = 2
                yroin = 0
                norb(0,0)
                norb(4,0)
                norb(2,0)
                norb(3,0)
                
        numero_tour+=1
        if tour == "noir":
            tour = "blanc"
        else:
            tour = "noir"
        affcoup()
        
        
        
def lookfor(c):
    global mat
    for a in range(8):
        for b in range(8):
            if mat[a][b] == c:
                return [b,a]
    return[]
    
    
    
def affcoup():
    # affiche les 16 derniers tours (un coup blanc et un coup noir)
    global numero_tour, lmemoire    
    if numero_tour >= 32:
        nbt = 16
    else:
        if numero_tour%2==1:
            nbt = int((numero_tour-1)/2)
        else:
            nbt = int(numero_tour/2)
    texte = ""
    k = numero_tour-1
    canvas.create_rectangle(326,10,475,30, fill = "white", outline="white")
    da=0
    if numero_tour%2==1:
        texte = str(int((numero_tour+1)/2)) + ". "
        texte += coup(lmemoire[k])
        canvas.create_text(400,20, text = texte)
        canvas.create_rectangle(326,30,475,50, fill = "white", outline="white")
        da = 1
        
        
    for a in range(nbt):
        texte = str(int((numero_tour-da)/2-a)) + ". " + coup(lmemoire[k-2*a-1-da]) + "  " + coup(lmemoire[k-2*a-da])
        canvas.create_rectangle(328,20*(a+da)+10,470,20*(a+da)+30, fill = "white", outline="white")
        canvas.create_text(400,20*(a+da)+20, text = texte)
        canvas.create_rectangle(328,20*(a+da)+30,470,20*(a+da)+50, fill = "white", outline="white")
    
    
    
def coup(l):
    # affiche un coup en fonction de la liste qu,on lui donne
    if len(l) == 6:
        t = let(l[5]) + coord(l[3],l[4]) + " " + signe(l[2]) + " " + coord(l[0],l[1])
    elif len(l) == 12:
        t = "O-O"
    elif len(l) == 15:
        t = "O-O-O"
    return t
    
    
    
def let(a):
    # pour determiner l'initiale de la piece qui se deplace (pur affichage)
    if a==0 or a == 11 or a == 21:
        return ""
    elif a == 12 or a == 22:
        return "K"
    elif a == 13 or a == 23:
        return "Q"
    elif a == 14 or a == 24:
        return "B"
    elif a == 15 or a == 25:
        return "N"
    elif a == 16 or a == 26:
        return "R"
     
     
        
def coord(a,b):
    # pour transformer des coordonnées 2-3 en c4 (pur affichage)
    letter = ["a","b","c","d","e","f","g","h"]
    return letter[b] + str(a+1)
    
def signe(a):
    # pour savoir si on a manger une piece ou pas (pur affichage)
    if a != 0:
        return "x"
    else:
        return "-"

def norb(x,y):
    # permet de rafficher une case particuliere de l'echequier (utile pour passer de orange a rien du tout)
    if (x+y)%2 == 0:
        bn = "#000000f00"
    else:
        bn = "#fffffffff"
    piece(x,y,bn)
    
def reinit():
    # permet d'afficher tout le plateau en fonction de ce qu'il y a dans la matrice
    for a in range(8):
        for b in range(8):
            
            norb(a,b)

def quitter(event):
    tk.destroy()
    
    
    
tk = Tk()
canvas = Canvas(tk,width = 475, height = 325, bd = 0, bg = "white")
canvas.pack(padx = 10, pady = 10)

tk.title("chess")
canvas.create_rectangle(4,4,325,325,fill = "white", outline = "black")
var()
reinit()
selectpiece()

tk.mainloop()

"""
Problèmes :
Pas de Promotion de pions sur la dernière ligne
Problème d’affichage des coups quand on passe au 10 ème coup
Prise en passant inexistante
Pas de mat défini
Pas de pat défini

Améliorations :
Peut-être faire un menu? Avec différentes parties enregistrées dans un fichier .txt
à partir des noms des coups, bouger les pièces?

Résolus :
pb quand on clique sur l'afficheur de coups

Améliorations faites :
Utiliser des sprites (images) plus que des lettres car plus facile à visualiser.

"""


