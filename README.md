# File Encryption & Decryption Windows App - Caesar & Vigenère Cipher (Tkinter GUI)

Ky është një aplikacion desktop i ndërtuar me Python dhe Tkinter, që ofron enkriptim dhe dekriptim të fajllave duke përdorur algoritmet klasikë të kriptografisë: Caesar dhe Vigenère. Projekti është zhvilluar si pjesë e fazës së tretë të detyrës në lëndën Data Security, me qëllim ndërtimin e një aplikacioni Windows për sigurinë e të dhënave.


## Karakteristikat

* Zgjedhja e algoritmit të enkriptimit/dekriptimit: Caesar ose Vigenère
* Vendosja e çelësit (key) për secilin algoritëm
* Zgjedhja e fajllit hyrës për t’u enkriptuar/dekriptuar
* Përcaktimi i fajllit dalës ku do të ruhet përmbajtja e përpunuar
* Mundësia për të ruajtur një mesazh nga një TextBox në një fajll të jashtëm
* Ndërfaqe grafike miqësore për përdoruesin, e ndërtuar me Tkinter

## Përmbajtja e Aplikacionit
### Algoritmet:

* Caesar Cipher: Zhvendos çdo shkronjë për një numër fiks pozicionesh në alfabet, sipas një çelësi numerik.
* Vigenère Cipher: Përdor një fjalë si çelës. Çdo shkronjë zhvendoset në bazë të vlerës alfabetike të shkronjës përkatëse të çelësit.



### Funksionalitetet kryesore:

* Encrypt File – Enkripton përmbajtjen e një fajlli hyrës dhe e ruan në një fajll tjetër.
* Decrypt File – Dekripton një fajll të enkriptuar më parë.
* Save Message to File – Ruajtja e një mesazhi të shkruar në një TextBox në një fajll .txt.

## Udhëzime për Përdorim

1. Vendos çelësin (key):
    * Për Caesar, përdor një numër (p.sh. 3).
    * Për Vigenère, përdor një fjalë alfabetike (p.sh. secret).
2. Zgjedh algoritmin nga lista: Caesar ose Vigenère.

3. Zgjedh fajllin hyrës që do të enkriptohet ose dekriptohet.

4. Zgjedh rrugën e fajllit dalës ku do të ruhet përmbajtja e përpunuar.

5. Kliko butonin Encrypt File ose Decrypt File.

6. (Opsionale)Shkruaj një mesazh në TextBox dhe ruaje atë me Save Message to File.

## Shembull i Përdorimit
### Algoritmi Caesar
* Fajlli example.txt me përmbajtje: Hello, this is a secret message!
* Çelësi: 3 
* Rezultati: Khoor, wklv lv d vhfuhw phvvdjh!
* ### Algoritmi Vigenère
* Fajlli example.txt me përmbajtje: Hello, this is a secret message!
* Çelësi: secret
* Rezultati: Ziaos, lvoq mq e mwdvwl wicigqi!

*(_**Shënim**: rezultatet mund të ndryshojnë varësisht nga implementimi i algoritmit dhe ruajtja e karaktereve jokapitale_)*

## Shënime Shtesë
* Aplikacioni është zhvilluar për sisteme Windows.
* Është ndërtuar në gjuhën Python duke përdorur bibliotekën Tkinter për GUI.
* Fajllat duhet të jenë në format tekstual (UTF-8), pasi algoritmet punojnë me karaktere alfabetike.

# Punuan 
* Ardit Hyseni
* Arila Behrami
* Arisa Dragusha
* Erion Mehmeti