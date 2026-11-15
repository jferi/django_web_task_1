from app.models import Program, Velemeny

program=Program(orszag="Franciaország",varos="Párizs",latnivalo="Eiffel-torony",kep="eiffel.jpg",ar="15900",idopont="2026.12.05. 10:00",leiras="Feljutás a torony második szintjére idegenvezetővel, sorban állás nélkül.")
program.save()
program=Program(orszag="Olaszország",varos="Róma",latnivalo="Colosseum",kep="colosseum.jpg",ar="18500",idopont="2026.12.12. 9:30",leiras="Séta az ókori amfiteátrumban és a Forum Romanumon magyar nyelvű vezetéssel.")
program.save()
program=Program(orszag="Spanyolország",varos="Barcelona",latnivalo="Sagrada Família",kep="sagrada.jpg",ar="16900",idopont="2027.01.16. 11:00",leiras="Gaudí bazilikájának megtekintése belépővel és magyar nyelvű vezetéssel.")
program.save()
program=Program(orszag="Magyarország",varos="Budapest",latnivalo="Országház",kep="orszaghaz.jpg",ar="6500",idopont="2027.01.23. 14:00",leiras="Vezetett látogatás az Országházban, a Szent Korona megtekintésével.")
program.save()
program=Program(orszag="Ausztria",varos="Bécs",latnivalo="Schönbrunni kastély",kep="schonbrunn.jpg",ar="12900",idopont="2027.02.06. 10:30",leiras="A császári lakosztályok és a kastélypark bejárása idegenvezetővel.")
program.save()
program=Program(orszag="Csehország",varos="Prága",latnivalo="Károly híd",kep="karolyhid.jpg",ar="8900",idopont="2027.02.20. 15:00",leiras="Belvárosi séta az Óvárostól a Károly hídon át a várig.")
program.save()

velemeny=Velemeny(nev="Kovács Anna",szoveg="A római program nagyon jól szervezett volt, az idegenvezető mindent elmagyarázott.")
velemeny.save()
velemeny=Velemeny(nev="Nagy Péter",szoveg="Párizsban tényleg nem kellett sorban állni, csak ajánlani tudom.")
velemeny.save()
