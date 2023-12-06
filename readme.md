# Databaser och python

**Betyg**: G/VG - Individuell betygsättning

- För att få G behöver ni implementera 90% av alla G-funktioner och visa på förståelse när ni förklarar hur ni modellerat och designat databasen
- För att få VG måste samtliga G-uppgifter & VG-funktioner vara gjorda, ni måste visa på en genomtänkt databasdesign och ni ska ha implementerat VG-delen på ett grundläggande sätt utifrån punkterna listade i filen.

**Deadline**: 2023-12-14 23:59 (Torsdag den 14e december)

## Beskrivning av uppgiften - Läs detta först

Uppgiften består av tre delar, först ett modelleringssteg och implementationssteg, sedan en muntlig redovisning där ni förväntas spela in en video med en demo av applikationen.  

1. Ni ska dela upp er i grupper om **2 personer**. Jag vill inte få förfrågningar om att vara fler eller själv, det nekas om det inte är ojämnt elever. Ni registrerar er grupp här:
https://docs.google.com/spreadsheets/d/1TMXTCdPKDl_ToE7kMRZ3SbGvLXBofycyUBgb0bVl4h0/edit?usp=sharing

********************************Github classroom********************************
Ni accepterar er laborationsuppgift på github classroom här:
https://classroom.github.com/a/rmpnpa8V
- tänk på att **båda** ska acceptera uppgiften, där den första får skapa en grupp, som sedan den andra personen får “joina”:
2. Gå igenom steg 1 - 3 listat längre ned i uppgiften.
3. Spela in en cirka **20-35 minuter** lång video där ni sitter tillsammans och båda är synliga i en kamera. Mer om det i sektionen “Videopresentation” längst ner

## Case - Bostadsannonser

Ni har fått i uppdrag att modellera och implementera en enklare applikation för att hantera en hemsida som **liknar** [hemnet.se](http://hemnet.se) - dvs. en annonssida för köp och sälj av bostäder.

Ni ska inkludera tabeller kopplat till följande koncept:

- Listings (Bostadsannonser)
- Category (Bostäder kan ha en kategori, tex. hus, lägenhet)
- Broker (Mäklare), en bostad kan ha en, och endast en, mäklare i detta system
- Customer (Ni kan se det som en User / Användare som vill köpa en bostad)
- En customer kan skapa appointments / intresseanmälningar för många bostäder, och en bostad kan vice versa ha intresseanmälningar från många customers
- En customer favorisera / favorita en bostadsannons

*Det är också OK att implementera fler tabeller om ni hinner / vill, som vanligt har ni en del frihet, ni kan ta inspiration av hemnet*

### Del 1 (G) - Modellera databasen

Använd drawsql eller [diagrams.net](http://diagrams.net) för att modellera databasen. Ni behöver inte ha med ett överflöd av attribut / kolumner för varje tabell, försök tänka “lagom”.

### Del 2 (G) - Implementera applikationen

Implementera funktionerna i [database.py](http://database.py) och [main.py](http://main.py) - ni kan också lägga till fler om ni vill.

### Del 3 - VG

Implementera funktionerna i vg[.py](http://database.py) - denna applikation kräver ingen meny eller frontend, utan ni ska visa att ni behärskar att skapa endpoints för CRUD-operationer i ett rest-api.

## Videopresentation - Detta gör ni i slutet efter steg 1 - 3

Ni ska spela in en cirka 20-35 minuter lång video där ni presenterar / visar en demo av er applikation. Ni ska inte utnyttja en powerpoint, utan fokus är på ert databasdiagram och koden.

Här kan ni hitta en enkel tutorial för att spela in video med facecam: https://www.youtube.com/watch?v=uL8BwstqiqE&ab_channel=KevinStratvert
Den ska laddas upp på **youtube** som en **[unlisted video](https://www.youtube.com/watch?v=AoRGSTPB9xs&ab_channel=WhatVwant-ATechnologyVlog)** som går att få tillgång via en länk (välj “unlisted”) och lägg länken i filen **videolink.txt** i ert repository så att jag hittar er video

**I videon ska ni inkludera följande segment:**
1. En inledande del där ni pratar om hur ni modellerat databasen, bonus om ni inte låter scriptade utan kan prata om det lite mer informellt. **Max 10 minuter.**
2. Ett segment där ni pratar om G-uppgiften, där varje person åtminstone ska prata om 3 funktioner var. **Max 10 - 15 minuter**
3. Ett segment om VG-uppgiften, där varje person åtminstone ska prata om 3 funktioner var. **(Max 10 - 15 minuter)**

*Det är helt OK att “klippa” videon, om ni tex. gjort del 1 & 2 och sedan vill klippa in del 3, bara ni inte redigerar videon överdrivet.*

När ni presenterar G & VG-delarna så vill jag att ni försöker tänka att ni ska presentera det för en annan utvecklare - vad är viktigt för utvecklaren att förstå? Förklara stukturen på er databas, programmet och varför ni implementerat saker på det sätt ni gjort. Försök att visa att ni har förståelse för koden, och argumentera för varför ni gjort på olika sätt.

**Tänk på att**:

- Ert diagram och kod ska vara tydligt synlig på videon, dvs. att ni zoomar in och att upplösningen är minst 720p
- Att ni båda tydligt ska höras
- Att båda ska få ordentliga chanser att prata
- Att ni kollat igenom videon och säkertställt att allt ser bra ut