# Recepty z pořadu Peče celá země

Jednoduchý kód slouží ke stažení všech receptů z české TV show a jejich přípavě do formátu pro tisk. Jedná se o rychle vytvořený jednoúčelový kód, který by se ale mohl hodit více lidem. Například, pokud vaše drahá polovička ráda peče. :)


### Příprava

Vytvořený scraper potřebuje python [Scrapy](https://scrapy.org/) framework. Scrapy lze nainstalovat pomocí jednoho z následujících způsobů.

```
sudo apt install python3-scrapy
```
nebo
```
sudo apt install python-pip
pip install scrapy
```

### Spuštění

```
scrapy runspider pece-cele-cesko-spider.py
```

### Další kroky

Výsledný html soubor využívá připravený style.css pro formátování. Vygenerovaný html soubor lze otevřít v prohlížeči, uložit (uloží se i včetně obrázků, které scraper nestahuje), nebo jeho obsah z prohlížeče (např. Google Chrome) zkopírovat do textového editoru (např. LibreOffice Writer). 
Soubor template.odt obsahuje připravený soubor s následujícími vlastnostmi.
* odlišné okraje pro liché a sudé stránky pro oboustraný tisk a následnou vazbu
* zalamování stránek před každým napisem h2 (název receptu)
* číslování stránek
* připravený obsah, který stačí pouze zaktualizovat


