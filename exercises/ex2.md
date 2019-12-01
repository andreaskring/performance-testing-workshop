## Ex 2

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

### CSV-filen med brugere

Hent CSV-filen med brugere [her](../jmeter/users.csv).

### Oprettelse af setUp Thread Group
1.  Start Alfresco:

    ```
    $ cd docker/alfresco
    $ docker-compose up
    ```

    Alfresco lytter nu på port 8080 på localhost.

1.  Opret en _setUp Thread Group_, som opretter brugerne i CSV-filen. Brug følgende endpoint 
    til at oprette brugere:

    ```
    POST /alfresco/s/api/people
    {
      "userName": "username"
      "firstName": "firstname",
      "lastName": "lastname",
      "email": "user@example.org",
      "password": "secret"
    }
    ```
1. 