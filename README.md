
### Database for a Course management system

 have python installed

 run 
 - pip install oracledb

 - pip nstall tkinter

 run the code from main.py

#### Creating of the tables

#### <i>Client Table</i>
```
CREATE TABLE Client (clientNo NUMBER PRIMARY KEY, clientName VARCHAR2(255) NOT NULL, clientStreet VARCHAR2(255), clientCity VARCHAR2(255), clientState VARCHAR2(255), clientZipCode VARCHAR2(10), attTelNo VARCHAR2(20), attFaxNo VARCHAR2(20), attEmailAddress VARCHAR2(255));
```

#### <i>Delegate Table</i>
```
CREATE TABLE Delegate (delegateNo NUMBER PRIMARY KEY, delegateTitle VARCHAR2(50), delegateFName VARCHAR2(255) NOT NULL, delegateLName VARCHAR2(255) NOT NULL, delegateStreet VARCHAR2(255), delegateCity VARCHAR2(255), delegateState VARCHAR2(255), delegateZipCode VARCHAR2(10), attTelNo VARCHAR2(20), attFaxNo VARCHAR2(20), attEmailAddress VARCHAR2(255), clientNo NUMBER, FOREIGN KEY (clientNo) REFERENCES Client(clientNo));
```

#### <i>Employee Table</i>
```
CREATE TABLE Employee (employeeNo NUMBER PRIMARY KEY, employeeName VARCHAR2(255) NOT NULL, employeePosition VARCHAR2(255));
```

#### <i>Location Table</i>
```
CREATE TABLE Location (locationNo NUMBER PRIMARY KEY, locationName VARCHAR2(255) NOT NULL, maxSize NUMBER);
```

#### <i>CourseType Table</i>
```
CREATE TABLE CourseType (courseTypeNo NUMBER PRIMARY KEY, courseTypeDescription VARCHAR2(255) NOT NULL);
```

#### <i>Course Table</i>
```
CREATE TABLE Course (courseNo NUMBER PRIMARY KEY, courseName VARCHAR2(255) NOT NULL, courseDescription VARCHAR2(255), startDate DATE, startTime TIMESTAMP, endDate DATE, endTime TIMESTAMP, maxDelegates NUMBER, confirmed CHAR(1) CHECK (confirmed IN ('Y', 'N')), delivererEmployeeNo NUMBER, courseTypeNo NUMBER, FOREIGN KEY (delivererEmployeeNo) REFERENCES Employee(employeeNo), FOREIGN KEY (courseTypeNo) REFERENCES CourseType(courseTypeNo));
```

#### <i>CourseFee Table</i>
```
CREATE TABLE CourseFee (courseFeeNo NUMBER PRIMARY KEY, feeDescription VARCHAR2(255), fee NUMBER, courseNo NUMBER, FOREIGN KEY (courseNo) REFERENCES Course(courseNo));
```

#### <i>Booking Table</i>
```
CREATE TABLE Booking (bookingNo NUMBER PRIMARY KEY, bookingDate DATE, locationNo NUMBER, courseNo NUMBER, bookingEmployeeNo NUMBER, FOREIGN KEY (locationNo) REFERENCES Location(locationNo), FOREIGN KEY (courseNo) REFERENCES Course(courseNo), FOREIGN KEY (bookingEmployeeNo) REFERENCES Employee(employeeNo));
```

#### <i>PaymentMethod Table</i>
```
CREATE TABLE PaymentMethod (pMethodNo NUMBER PRIMARY KEY, methodDescription VARCHAR2(255) NOT NULL);
```

#### <i>Registration Table</i>
```
CREATE TABLE Registration (registrationNo NUMBER PRIMARY KEY, registrationDate DATE, delegateNo NUMBER, courseFeeNo NUMBER, registerEmployeeNo NUMBER, courseNo NUMBER, FOREIGN KEY (delegateNo) REFERENCES Delegate(delegateNo), FOREIGN KEY (courseFeeNo) REFERENCES CourseFee(courseFeeNo), FOREIGN KEY (registerEmployeeNo) REFERENCES Employee(employeeNo), FOREIGN KEY (courseNo) REFERENCES Course(courseNo));
```

#### <i>Invoice Table</i>
```
CREATE TABLE Invoice (invoiceNo NUMBER PRIMARY KEY, dateRaised DATE, datePaid DATE, creditCardNo VARCHAR2(20), holdersName VARCHAR2(255), expiryDate DATE, registrationNo NUMBER, pMethodNo NUMBER, FOREIGN KEY (registrationNo) REFERENCES Registration(registrationNo), FOREIGN KEY (pMethodNo) REFERENCES PaymentMethod(pMethodNo));
```


#### <i>Insert record -- stored procedures</i>
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
 ![alt text](<screenshots/Screenshot (28).png>)
 ![alt text](<screenshots/Screenshot (29).png>)

#### <i>Retrieve record -- cursors</i>
```

CREATE OR REPLACE PROCEDURE retrieve_delegate(
    p_delegate_no IN NUMBER,
    p_title OUT VARCHAR2,
    p_first_name OUT VARCHAR2,
    p_last_name OUT VARCHAR2,
    p_street OUT VARCHAR2,
    p_city OUT VARCHAR2,
    p_state OUT VARCHAR2,
    p_zip_code OUT VARCHAR2,
    p_tel_no OUT VARCHAR2,
    p_fax_no OUT VARCHAR2,
    p_email_address OUT VARCHAR2,
    p_client_no OUT NUMBER,
    p_success OUT VARCHAR2,
    p_error_msg OUT VARCHAR2
) AS
    v_count NUMBER;

BEGIN
    SELECT COUNT(*) INTO v_count FROM Delegate WHERE delegateNo = p_delegate_no;

    IF v_count = 1 THEN
        SELECT delegateTitle, delegateFName, delegateLName, delegateStreet, delegateCity, delegateState, delegateZipCode, attTelNo, attFaxNo, attEmailAddress, clientNo  INTO p_title, p_first_name, p_last_name, p_street, p_city, p_state, p_zip_code, p_tel_no, p_fax_no, p_email_address, p_client_no 
        FROM Delegate WHERE delegateNo = p_delegate_no;

        p_success := 'Success';
        p_error_msg := NULL;

    ELSE
        p_title := NULL;
        p_first_name := NULL;
        p_last_name := NULL;
        p_street := NULL;
        p_city := NULL;
        p_state := NULL;
        p_zip_code := NULL;
        p_tel_no := NULL;
        p_fax_no := NULL;
        p_email_address := NULL;
        p_client_no := NULL;
        p_success := 'Error';
        p_error_msg := 'Delegate not found.';
    END IF;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        p_title := NULL;
        p_first_name := NULL;
        p_last_name := NULL;
        p_street := NULL;
        p_city := NULL;
        p_state := NULL;
        p_zip_code := NULL;
        p_tel_no := NULL;
        p_fax_no := NULL;
        p_email_address := NULL;
        p_client_no := NULL;
        p_success := 'Error';
        p_error_msg := 'Delegate not found.';
    WHEN OTHERS THEN
        p_title := NULL;
        p_first_name := NULL;
        p_last_name := NULL;
        p_street := NULL;
        p_city := NULL;
        p_state := NULL;
        p_zip_code := NULL;
        p_tel_no := NULL;
        p_fax_no := NULL;
        p_email_address := NULL;
        p_client_no := NULL;
        p_success := 'Error';
        p_error_msg := SQLERRM;
END retrieve_delegate;
/
```
![alt text](<screenshots/Screenshot (30).png>)
![alt text](<screenshots/Screenshot (31).png>)

#### <i>Update record -- stored procedures</i>

```
CREATE OR REPLACE PROCEDURE update_delegate(
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
    UPDATE Delegate
    SET delegateTitle = p_delegateTitle,
        delegateFName = p_delegateFName,
        delegateLName = p_delegateLName,
        delegateStreet = p_delegateStreet,
        delegateCity = p_delegateCity,
        delegateState = p_delegateState,
        delegateZipCode = p_delegateZipCode,
        attTelNo = p_attTelNo,
        attFaxNo = p_attFaxNo,
        attEmailAddress = p_attEmailAddress,
        clientNo = p_clientNo
    WHERE delegateNo = p_delegateNo;
    COMMIT;

EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20005, 'No data found for the provided delegateNo.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20006, 'Error updating delegate: ' || SQLERRM);
END;
```
![alt text](<screenshots/Screenshot (32).png>)
![alt text](<screenshots/Screenshot (33).png>)
![alt text](<screenshots/Screenshot (34).png>)

#### <i>delete record -- stored procedures</i>

```
CREATE OR REPLACE PROCEDURE delete_delegate(
    p_delegateNo IN NUMBER
) AS
BEGIN
    DELETE FROM Delegate WHERE delegateNo = p_delegateNo;
    COMMIT;
EXCEPTION
    WHEN NO_DATA_FOUND THEN
        RAISE_APPLICATION_ERROR(-20007, 'No data found for the provided delegateNo.');
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20008, 'Error deleting delegate: ' || SQLERRM);
END;
```
![alt text](<screenshots/Screenshot (34)-1.png>)
![alt text](<screenshots/Screenshot (35).png>)
![alt text](<screenshots/Screenshot (36).png>)

#### <i>Triggers to log user activities on a specified table into a log table</i>

```
CREATE TABLE Delegate_Log (
    log_id           NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    operation_type   VARCHAR2(10),  -- Type of operation (INSERT, UPDATE, DELETE)
    delegate_no      NUMBER,
    delegate_title   VARCHAR2(10),
    delegate_fname   VARCHAR2(50),
    delegate_lname   VARCHAR2(50),
    operation_time   TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Time of the operation
    username         VARCHAR2(30)  -- User who performed the operation
);
```

```
CREATE OR REPLACE TRIGGER trg_delegate_after_insert
AFTER INSERT ON Delegate
FOR EACH ROW
BEGIN
    INSERT INTO Delegate_Log (
        operation_type,
        delegate_no,
        delegate_title,
        delegate_fname,
        delegate_lname,
        operation_time,
        username
    ) VALUES (
        'INSERT',
        :NEW.delegateNo,
        :NEW.delegateTitle,
        :NEW.delegateFName,
        :NEW.delegateLName,
        SYSTIMESTAMP,
        USER
    );
END;
```

```
CREATE OR REPLACE TRIGGER trg_delegate_after_update
AFTER UPDATE ON Delegate
FOR EACH ROW
BEGIN
    INSERT INTO Delegate_Log (
        operation_type,
        delegate_no,
        delegate_title,
        delegate_fname,
        delegate_lname,
        operation_time,
        username
    ) VALUES (
        'UPDATE',
        :NEW.delegateNo,
        :NEW.delegateTitle,
        :NEW.delegateFName,
        :NEW.delegateLName,
        SYSTIMESTAMP,
        USER
    );
END;
```

```
CREATE OR REPLACE TRIGGER trg_delegate_after_delete
AFTER DELETE ON Delegate
FOR EACH ROW
BEGIN
    INSERT INTO Delegate_Log (
        operation_type,
        delegate_no,
        delegate_title,
        delegate_fname,
        delegate_lname,
        operation_time,
        username
    ) VALUES (
        'DELETE',
        :OLD.delegateNo,
        :OLD.delegateTitle,
        :OLD.delegateFName,
        :OLD.delegateLName,
        SYSTIMESTAMP,
        USER
    );
END;
```

![alt text](<screenshots/Screenshot (37).png>)

#### <i>BackUp</i>
```
CREATE OR REPLACE PROCEDURE backup_database(
    p_backup_dir IN VARCHAR2,
    p_backup_file IN VARCHAR2
) AS
BEGIN
    EXECUTE IMMEDIATE 'CREATE BACKUPSET AS BACKUP DATABASE TO ''' || p_backup_dir || '/' || p_backup_file || '''';
    COMMIT;
EXCEPTION
    WHEN OTHERS THEN
        RAISE_APPLICATION_ERROR(-20008, 'Error creating database backup: ' || SQLERRM);
END;
```