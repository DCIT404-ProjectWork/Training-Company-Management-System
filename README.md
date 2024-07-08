
### Database for a Course management system

 have python installed

 run 
 - pip install oracledb

 - pip nstall tkinter

 run the code from main.py

##### <i>Insert record -- stored procedures</i>
```
CREATE OR REPLACE PROCEDURE insert_delegate(

    p_delegateNo IN NUMBER,
    p_delegateTitle IN VARCHAR2,
    p_delegateFName IN VARCHAR2,
    p_delegateLName IN VARCHAR2,
    p_delegateStreet IN VARCHAR2,
    p_delegateCity IN VARCHAR2,
    p_delegateState IN VARCHAR2,
    p_delegateZipCode IN VARCHAR2,
    p_attTelNo IN VARCHAR2,
    p_attFaxNo IN VARCHAR2,
    p_attEmailAddress IN VARCHAR2,
    p_clientNo IN NUMBER

) AS

BEGIN
    INSERT INTO Delegate (delegateNo, delegateTitle, delegateFName, delegateLName, delegateStreet, delegateCity, delegateState, delegateZipCode, attTelNo, attFaxNo, attEmailAddress, clientNo)
    VALUES (p_delegateNo, p_delegateTitle, p_delegateFName, p_delegateLName, p_delegateStreet, p_delegateCity, p_delegateState, p_delegateZipCode, p_attTelNo, p_attFaxNo, p_attEmailAddress, p_clientNo);

    COMMIT;

EXCEPTION
    WHEN DUP_VAL_ON_INDEX THEN
        RAISE_APPLICATION_ERROR(-20001, 'Delegate No already exists.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20002, 'Error inserting delegate: ' || SQLERRM);
END;
```
 
 ![alt text](<Screenshot (27).png>)