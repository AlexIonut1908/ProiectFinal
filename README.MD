* Structura unui framework BDD:

 1. Folder features - Feature files - contine fisiere scrise intru-un limbaj mai natural (gherkin) care sa descrie scenariile de business
     - Given (contextul in care se desfasoara actiunea)
     - When (este urmat de actiunea pe care o facem)
     - Then (deznodamant - verificarea pe care vrem sa o facem)
    
 2. Folder steps - Step definition files - maparea tehnica a fisierelor de business - feature files

 3. Folder pages - Pagini de mapare pentru elementele din browser (POM - page object model)
     - Vom avea fisiere pentru fiecare pagina web a aplicatiei
     - base_page file - este o clasa ce contine metode care pot fi folosite in mai multe clase (care sunt utile pentru toate paginile)
 
 4. Fisier browser - Contine insctructiuni de instalare si deschidere browser

 5. Fisier environment - Contine instantierea tuturor claselor de tip pages

 * Metodologii de lucru:

 1. Waterfall:
     - stricta
     - orice modificare necesara dupa inceperea proiectului va trebui implementata intr-un proiect nou
     - se planuieste tot la inceput, apoi se dezvolta, apoi se testeaza si apoi se da in piata
     - feedback-ul pentru produs de la clienti se primeste tarziu, la final
     - de regula se dezvolta multa functionalitate

 2. Agile:
     - mai putin stricta, este flexibila si organizata
     - orice modificare aparuta in timpul implementarii, se poate modifica pe parcurs
     - se lucreaza in sprint-uri (de regula sunt cicluri de doua saptamani)
     - intr-un sprint se planifica, se dezvolta, se testeaza si se da in piata (clientului)
     - feedback-ul pentru produs de la client se primeste dupa fiecare sprint si se poate implementa in urmatoarele sprint-uri
     - (Scrum si Kanban, Scrumban)

 * Functionalitatile se pot grupa in felul urmator:

 1. Epic -> componente majore (ex: pagina de cumparaturi)
 2. Story -> functionalitati independente din aceasi componenta (ex: adaugarea in cos, filtre)

 * User story:

 - As a customer I want to view all electronics products.
 - As a customer I want to add a product to my shopping cart.
 - As a {user} I want to {action} (so that I can {reason}).

Comanda: behave -f html -o behave.report.html --tags=smoke