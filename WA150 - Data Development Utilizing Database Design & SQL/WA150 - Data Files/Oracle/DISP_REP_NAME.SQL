CREATE OR REPLACE PROCEDURE DISP__REP_NAME(I_REP_NUM IN REP.REP_NUM%TYPE) AS
  I_LAST_NAME REP.LAST_NAME%TYPE;
  I_FIRST_NAME REP.FIRST_NAME%TYPE;
  
  BEGIN
  SELECT LAST_NAME, FIRST_NAME
  INTO I_LAST_NAME, I_FIRST_NAME
  FROM REP
  WHERE REP_NUM = I_REP_NUM;
  
  DBMS_OUTPUT.PUT_LINE(RTRIM(I_FIRST_NAME)|| ' '||RTRIM(I_LAST_NAME));
  
  END;
  /