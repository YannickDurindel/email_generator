#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 12:19:43 2022

@author: yannick
"""
import subprocess
import time

t0 = time.time()

def telnet_gmail_smtp(email):
    command = "telnet gmail-smtp-in.l.google.com 25"
    process = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    process.stdin.write(b'EHLO Buddy\n')
    process.stdin.flush()
    process.stdin.write(b'MAIL FROM:<yannick.durindel@gmail.com>\n')
    process.stdin.flush()
    email = bytes(email,'UTF-8')
    command = b'RCPT TO: <'+email+b'>\n'
    process.stdin.write(command)
    process.stdin.flush()
    process.stdin.write(b'QUIT\n')
    process.stdin.flush()
    for line in iter(process.stdout.readline, b''):
        if line[10:-12] == b'The email account that you tried to reach does not exist.':
            return False
    return True

def listcreat(text):
    liste = []
    n = 0
    for i in range (0,len(text)-1):
        if text[i]=="ü":
            text = text[0:i]+"u"+text[i+1:len(text)]
        if text[i]=="é":
            text = text[0:i]+"e"+text[i+1:len(text)]
        if text[i]=="í":
            text = text[0:i]+"i"+text[i+1:len(text)]
        if text[i]=="è":
            text = text[0:i]+"e"+text[i+1:len(text)]            
        if text[i+1]=="\n" or text[i+1]==",":
            string = text[n:i+1]
            string = string.lower()
            if text[n-1] == ",":
                string = string[1:len(string)]
            liste.append(string)
            n = i+2
    return liste

prenom = """Michael
Christopher
Jessica
Matthew
Ashley
Jennifer
Joshua
Amanda
Daniel
David
James
Robert
John
Joseph
Andrew
Ryan
Brandon
Jason
Justin
Sarah
William
Jonathan
Stephanie
Brian
Nicole
Nicholas
Anthony
Heather
Eric
Elizabeth
Adam
Megan
Melissa
Kevin
Steven
Thomas
Timothy
Christina
Kyle
Rachel
Laura
Lauren
Amber
Brittany
Danielle
Richard
Kimberly
Jeffrey
Amy
Crystal
Michelle
Tiffany
Jeremy
Benjamin
Mark
Emily
Aaron
Charles
Rebecca
Jacob
Stephen
Patrick
Sean
Erin
Zachary
Jamie
Kelly
Samantha
Nathan
Sara
Dustin
Paul
Angela
Tyler
Scott
Katherine
Andrea
Gregory
Erica
Mary
Travis
Lisa
Kenneth
Bryan
Lindsey
Kristen
Jose
Alexander
Jesse
Katie
Lindsay
Shannon
Vanessa
Courtney
Christine
Alicia
Cody
Allison
Bradley
Samuel
Shawn
April
Derek
Kathryn
Kristin
Chad
Jenna
Tara
Maria
Krystal
Jared
Anna
Edward
Julie
Peter
Holly
Marcus
Kristina
Natalie
Jordan
Victoria
Jacqueline
Corey
Keith
Monica
Juan
Donald
Cassandra
Meghan
Joel
Shane
Phillip
Patricia
Brett
Ronald
Catherine
George
Antonio
Cynthia
Stacy
Kathleen
Raymond
Carlos
Brandi
Douglas
Nathaniel
Ian
Craig
Brandy
Alex
Valerie
Veronica
Cory
Whitney
Gary
Derrick
Philip
Luis
Diana
Chelsea
Leslie
Caitlin
Leah
Natasha
Erika
Casey
Latoya
Erik
Dana
Victor
Brent
Dominique
Frank
Brittney
Evan
Gabriel
Julia
Candice
Karen
Melanie
Adrian
Stacey
Margaret
Sheena
Wesley
Vincent
Alexandra
Katrina
Bethany
Nichole
Larry
Jeffery
Curtis
Carrie
Todd
Blake
Christian
Randy
Dennis
Alison
Trevor
Seth
Kara
Joanna
Rachael
Luke
Felicia
Brooke
Austin
Candace
Jasmine
Jesus
Alan
Susan
Sandra
Tracy
Kayla
Nancy
Tina
Krystle
Russell
Jeremiah
Carl
Miguel
Tony
Alexis
Gina
Jillian
Pamela
Mitchell
Hannah
Renee
Denise
Molly
Jerry
Misty
Mario
Johnathan
Jaclyn
Brenda
Terry
Lacey
Shaun
Devin
Heidi
Troy
Lucas
Desiree
Jorge
Andre
Morgan
Drew
Sabrina
Miranda
Alyssa
Alisha
Teresa
Johnny
Meagan
Allen
Krista
Marc
Tabitha
Lance
Ricardo
Martin
Chase
Theresa
Melinda
Monique
Tanya
Linda
Kristopher
Bobby
Caleb
Ashlee
Kelli
Henry
Garrett
Mallory
Jill
Jonathon
Kristy
Anne
Francisco
Danny
Robin
Lee
Tamara
Manuel
Meredith
Colleen
Lawrence
Christy
Ricky
Randall
Marissa
Ross
Mathew
Jimmy
Abigail
Kendra
Carolyn
Billy
Deanna
Jenny
Jon
Albert
Taylor
Lori
Rebekah
Cameron
Ebony
Wendy
Angel
Micheal
Kristi
Caroline
Colin
Dawn
Kari
Clayton
Arthur
Roger
Roberto
Priscilla
Darren
Kelsey
Clinton
Walter
Louis
Barbara
Isaac
Cassie
Grant
Cristina
Tonya
Rodney
Bridget
Joe
Cindy
Oscar
Willie
Maurice
Jaime
Angelica
Sharon
Julian
Jack
Jay
Calvin
Marie
Hector
Kate
Adrienne
Tasha
Michele
Ana
Stefanie
Cara
Alejandro
Ruben
Gerald
Audrey
Kristine
Ann
Shana
Javier
Katelyn
Brianna
Bruce
Deborah
Claudia
Carla
Wayne
Roy
Virginia
Haley
Brendan
Janelle
Jacquelyn
Beth
Edwin
Dylan
Dominic
Latasha
Darrell
Geoffrey
Savannah
Reginald
Carly
Fernando
Ashleigh
Aimee
Regina
Mandy
Sergio
Rafael
Pedro
Janet
Kaitlin
Frederick
Cheryl
Autumn
Tyrone
Martha
Omar
Lydia
Jerome
Theodore
Abby
Neil
Shawna
Sierra
Nina
Tammy
Nikki
Terrance
Donna
Claire
Cole
Trisha
Bonnie
Diane
Summer
Carmen
Mayra
Jermaine
Eddie
Micah
Marvin
Levi
Emmanuel
Brad
Taryn
Toni
Jessie
Evelyn
Darryl
Ronnie
Joy
Adriana
Ruth
Mindy
Spencer
Noah
Raul
Suzanne
Sophia
Dale
Jodi
Christie
Raquel
Naomi
Kellie
Ernest
Jake
Grace
Tristan
Shanna
Hilary
Eduardo
Ivan
Hillary
Yolanda
Alberto
Andres
Olivia
Armando
Paula
Amelia
Sheila
Rosa
Robyn
Kurt
Dane
Glenn
Nicolas
Gloria
Eugene
Logan
Steve
Ramon
Bryce
Tommy
Preston
Keri
Devon
Alana
Marisa
Melody
Rose
Barry
Marco
Karl
Daisy
Leonard
Randi
Maggie
Charlotte
"""

nom = """SMITH
JOHNSON
WILLIAMS
JONES
BROWN
DAVIS
MILLER
WILSON
MOORE
TAYLOR
ANDERSON
THOMAS
JACKSON
WHITE
HARRIS
MARTIN
THOMPSON
GARCIA
MARTINEZ
ROBINSON
CLARK
RODRIGUEZ
LEWIS
LEE
WALKER
HALL
ALLEN
YOUNG
HERNANDEZ
KING
WRIGHT
LOPEZ
HILL
SCOTT
GREEN
ADAMS
BAKER
GONZALEZ
NELSON
CARTER
MITCHELL
PEREZ
ROBERTS
TURNER
PHILLIPS
CAMPBELL
PARKER
EVANS
EDWARDS
COLLINS
STEWART
SANCHEZ
MORRIS
ROGERS
REED
COOK
MORGAN
BELL
MURPHY
BAILEY
RIVERA
COOPER
RICHARDSON
COX
HOWARD
WARD
TORRES
PETERSON
GRAY
RAMIREZ
JAMES
WATSON
BROOKS
KELLY
SANDERS
PRICE
BENNETT
WOOD
BARNES
ROSS
HENDERSON
COLEMAN
JENKINS
PERRY
POWELL
LONG
PATTERSON
HUGHES
FLORES
WASHINGTON
BUTLER
SIMMONS
FOSTER
GONZALES
BRYANT
ALEXANDER
RUSSELL
GRIFFIN
DIAZ
HAYES
MYERS
FORD
HAMILTON
GRAHAM
SULLIVAN
WALLACE
WOODS
COLE
WEST
JORDAN
OWENS
REYNOLDS
FISHER
ELLIS
HARRISON
GIBSON
MCDONALD
CRUZ
MARSHALL
ORTIZ
GOMEZ
MURRAY
FREEMAN
WELLS
WEBB
SIMPSON
STEVENS
TUCKER
PORTER
HUNTER
HICKS
CRAWFORD
HENRY
BOYD
MASON
MORALES
KENNEDY
WARREN
DIXON
RAMOS
REYES
BURNS
GORDON
SHAW
HOLMES
RICE
ROBERTSON
HUNT
BLACK
DANIELS
PALMER
MILLS
NICHOLS
GRANT
KNIGHT
FERGUSON
ROSE
STONE
HAWKINS
DUNN
PERKINS
HUDSON
SPENCER
GARDNER
STEPHENS
PAYNE
PIERCE
BERRY
MATTHEWS
ARNOLD
WAGNER
WILLIS
RAY
WATKINS
OLSON
CARROLL
DUNCAN
SNYDER
HART
CUNNINGHAM
BRADLEY
LANE
ANDREWS
RUIZ
HARPER
FOX
RILEY
ARMSTRONG
CARPENTER
WEAVER
GREENE
LAWRENCE
ELLIOTT
CHAVEZ
SIMS
AUSTIN
PETERS
KELLEY
FRANKLIN
LAWSON
FIELDS
GUTIERREZ
RYAN
SCHMIDT
CARR
VASQUEZ
CASTILLO
WHEELER
CHAPMAN
OLIVER
MONTGOMERY
RICHARDS
WILLIAMSON
JOHNSTON
BANKS
MEYER
BISHOP
MCCOY
HOWELL
ALVAREZ
MORRISON
HANSEN
FERNANDEZ
GARZA
HARVEY
LITTLE
BURTON
STANLEY
NGUYEN
GEORGE
JACOBS
REID
KIM
FULLER
LYNCH
DEAN
GILBERT
GARRETT
ROMERO
WELCH
LARSON
FRAZIER
BURKE
HANSON
DAY
MENDOZA
MORENO
BOWMAN
MEDINA
FOWLER
BREWER
HOFFMAN
CARLSON
SILVA
PEARSON
HOLLAND
DOUGLAS
FLEMING
JENSEN
VARGAS
BYRD
DAVIDSON
HOPKINS
MAY
TERRY
HERRERA
WADE
SOTO
WALTERS
CURTIS
NEAL
CALDWELL
LOWE
JENNINGS
BARNETT
GRAVES
JIMENEZ
HORTON
SHELTON
BARRETT
OBRIEN
CASTRO
SUTTON
GREGORY
MCKINNEY
LUCAS
MILES
CRAIG
RODRIQUEZ
CHAMBERS
HOLT
LAMBERT
FLETCHER
WATTS
BATES
HALE
RHODES
PENA
BECK
NEWMAN
HAYNES
MCDANIEL
MENDEZ
BUSH
VAUGHN
PARKS
DAWSON
SANTIAGO
NORRIS
HARDY
LOVE
STEELE
CURRY
POWERS
SCHULTZ
BARKER
GUZMAN
PAGE
MUNOZ
BALL
KELLER
CHANDLER
WEBER
LEONARD
WALSH
LYONS
RAMSEY
WOLFE
SCHNEIDER
MULLINS
BENSON
SHARP
BOWEN
DANIEL
BARBER
CUMMINGS
HINES
BALDWIN
GRIFFITH
VALDEZ
HUBBARD
SALAZAR
REEVES
WARNER
STEVENSON
BURGESS
SANTOS
TATE
CROSS
GARNER
MANN
MACK
MOSS
THORNTON
DENNIS
MCGEE
FARMER
DELGADO
AGUILAR
VEGA
GLOVER
MANNING
COHEN
HARMON
RODGERS
ROBBINS
NEWTON
TODD
BLAIR
HIGGINS
INGRAM
REESE
CANNON
STRICKLAND
TOWNSEND
POTTER
GOODWIN
WALTON
ROWE
HAMPTON
ORTEGA
PATTON
SWANSON
JOSEPH
FRANCIS
GOODMAN
MALDONADO
YATES
BECKER
ERICKSON
HODGES
RIOS
CONNER
ADKINS
WEBSTER
NORMAN
MALONE
HAMMOND
FLOWERS
COBB
MOODY
QUINN
BLAKE
MAXWELL
POPE
FLOYD
OSBORNE
PAUL
MCCARTHY
GUERRERO
LINDSEY
ESTRADA
SANDOVAL
GIBBS
TYLER
GROSS
FITZGERALD
STOKES
DOYLE
SHERMAN
SAUNDERS
WISE
COLON
GILL
ALVARADO
GREER
PADILLA
SIMON
WATERS
NUNEZ
BALLARD
SCHWARTZ
MCBRIDE
HOUSTON
CHRISTENSEN
KLEIN
PRATT
BRIGGS
PARSONS
MCLAUGHLIN
ZIMMERMAN
FRENCH
BUCHANAN
MORAN
COPELAND
ROY
PITTMAN
BRADY
MCCORMICK
HOLLOWAY
BROCK
POOLE
FRANK
LOGAN
OWEN
BASS
MARSH
DRAKE
WONG
JEFFERSON
PARK
MORTON
ABBOTT
SPARKS
PATRICK
NORTON
HUFF
CLAYTON
MASSEY
LLOYD
FIGUEROA
CARSON
BOWERS
ROBERSON
BARTON
TRAN
LAMB
HARRINGTON
CASEY
BOONE
CORTEZ
CLARKE
MATHIS
SINGLETON
WILKINS
CAIN
BRYAN
UNDERWOOD
HOGAN
MCKENZIE
COLLIER
LUNA
PHELPS
MCGUIRE
ALLISON
BRIDGES
WILKERSON
NASH
SUMMERS
ATKINS
"""

PRENOMS = listcreat(prenom)
NOMS = listcreat(nom)
text = []
email = []

for i in range(0,len(PRENOMS)):       #de 0 à 20 done
    for j in range(0,len(NOMS)): 
        if i*j>22000 and len(email)<12000:
            mail = PRENOMS[i]+NOMS[j]+"@gmail.com"
            if telnet_gmail_smtp(mail)==True:
                email.append(mail)
                text.append(PRENOMS[i]+","+NOMS[j]+","+mail+",yes,,,,,,,,,,,,,,,,")
            mail = PRENOMS[i][0]+NOMS[j]+"@gmail.com"
            if telnet_gmail_smtp(mail) == True:
                email.append(mail)
                text.append(PRENOMS[i][0]+","+NOMS[j]+","+mail+",yes,,,,,,,,,,,,,,,,")

try:
    with open('/home/yannick/Documents/useless/py_codes/Email_broadcast/email_list.txt', 'w') as email_list:
        for i in range(0,len(text)):
            email_list.write(text[i]+"\n")#text[i]+"\n")
except FileNotFoundError:
    print("The 'docs' directory does not exist")

print(time.time()-t0)