# Ex 2

Opsætning af en testplan, som indeholder lidt flere elementer. Vi laver nogle kald 
mod et standard Alfresco-system (leveres i Docker). Testplanen skal indeholde følgende 
elementer:

1. Et _Config Element_, som læser en række brugere fra en CSV-fil.
1. En _setUp Thread Group_ (der kun køres en enkelt gang), som opretter brugerne fra 
   CSV-filen i Alfresco.
1. En trådgruppe indeholdende requests, der:
    * Uploader et dokument med et tilfældigt navn.
    * Henter dokumentet igen.
    * Sletter dokumentet.

## Alfresco endpoints

Her følger en kort beskrivelse af de endpoints, vi får brug for at kalde i testplanen. Ved 
POST requestene er der i hvert tilfælde givet et eksempel på det JSON, der skal sendes.

### Oprettelse af brugere

```
POST /alfresco/s/api/people
{
  "userName": "username",
  "firstName": "firstname",
  "lastName": "lastname",
  "email": "username@example.org",
  "password": "secret"
}
```

### Tilføje brugere til et Alfresco site

Brugerne skal tilføjes til et _site_ i Alfresco. Vi anvender Alfrescos standard site, som 
har _site short name_, som er `swsdp`. For at tilføje en bruger til dette site kaldes:
```
POST /alfresco/s/api/sites/swsdp/memberships
{
  "role": "SiteManager",
  "person": {
  	"userName":"username"
  }
}
```

### Upload af dokument

Foretages vha. et multipart/form-data POST request til
```
POST /alfresco/s/api/upload
```
hvor e.g. følgende felter sendes med i formen:
```
siteid=swsdp
containerid=documentLibrary
filename=someFile.txt
filedata=(binary <- selve filen)
```

### Hente et dokument

```
GET /alfresco/s/api/node/content/workspace/SpacesStore/${nodeRef}
```

hvor `${nodeRef}` er referencen til den Alfresco _node_, hvor filen er gemt. 
Bemærk, at denne `NodeRef` returneres i ovenstående kald, hvor filen blev uploadet.

### Slette et dokument

```
DELETE /alfresco/api/-default-/public/alfresco/versions/1/nodes/${nodeRef}
```

hvor `${nodeRef}` på samme måde som før er referencen til den Alfresco node, 
hvor filen er gemt. 

## Testplanen

Gør nedenstående for af konstruere JMeter testplanen.

### CSV-filen med brugere

Hent CSV-filen med brugere [her](../jmeter/users.csv).

### Oprettelse af setUp Thread Group
1.  Start Alfresco:

    ```
    $ cd docker/alfresco
    $ docker-compose up
    ```

    Alfresco lytter nu på port 8080 på localhost.

1.  Lav en ny JMeter testplan.
1.  Tilføj et _HTTP Request Defaults_ element (findes under _Config Elements_) til 
    testplanen, og sæt værdierne for `Server Name` og `Port Number`.
1.  Tilføj en _CSV Data Set Config_ (også et Config Element) og brug denne til at 
    indlæse bruger og passwords 
    fra CSV-filen (udfyld felterne `Filename` og `Variable Names`).
1.  Tilføj et _View Results Tree_ til testplanen (findes under _Samplers_).
1.  Opret en _setUp Thread Group_, som skal oprette brugerne i CSV-filen.
1.  Tilføj en _Simple Controller_ til ovenstående trådgruppe (findes under 
    _Logic Controllers_).
1.  Tilføj en _HTTP Authorization Manager_ til controlleren og udfyld felterne 
    `Base URL=http://localhost:8080`), `Username=admin` og `Password=admin`.
1.  Tilføj en _HTTP Header Manager_ til controlleren og tilføj headeren 
    `Content-Type: application/json` til denne.
1.  Tilføj et _HTTP Request_ til controlleren, som opretter en bruger via informationer 
    i CSV-filen.
1.  Tilføj et HTTP Request til controlleren, som tilføjer brugeren til `swsdp` sitet 
    i Alfresco.

Verificér, at testplanen fungerer indtil videre.