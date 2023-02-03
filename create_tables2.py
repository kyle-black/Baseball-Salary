 commands = (
        """
        CREATE TABLE vendors (
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        """,
        """ CREATE TABLE parts (
                part_id SERIAL PRIMARY KEY,
                part_name VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE part_drawings (
                part_id INTEGER PRIMARY KEY,
                file_extension VARCHAR(5) NOT NULL,
                drawing_data BYTEA NOT NULL,
                FOREIGN KEY (part_id)
                REFERENCES parts (part_id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE vendor_parts (
                vendor_id INTEGER NOT NULL,
                part_id INTEGER NOT NULL,
                PRIMARY KEY (vendor_id , part_id),
                FOREIGN KEY (vendor_id)
                    REFERENCES vendors (vendor_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (part_id)
                    REFERENCES parts (part_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """)
        

         """
        CREATE TABLE seasons (
            Rk INTEGER PRIMARY KEY,
            Team VARCHAR(255) NOT NULL,
            Wins  INTEGER NOT NULL,
            Losses INTEGER NOT NULL,
            win_PCT NUMERIC(5,3) NOT NULL,
            Runs INTEGER NOT NULL,
            Runs_Allowed INTEGER NOT NULL,
            Runs_Diff NUMERIC(5,3) NOT NULL,
            SOS NUMERIC(5,3) NOT NULL,
            SRS NUMERIC(5,3) NOT NULL,
            pythWL VARCHAR(255) NOT NULL,
            vEAST VARCHAR(255) NOT NULL,
            vCENT VARCHAR(255)  NOT NULL,
            vWest VARCHAR(255)  NOT NULL,
            Inter VARCHAR(255) NOT NULL,
            Home VARCHAR(255) NOT NULL,
            Road VARCHAR(255) NOT NULL,
            ExInn VARCHAR(255) NOT NULL,
            1Run VARCHAR(255) NOT NULL,
            vRHP VARCHAR(255) NOT NULL,
            vLHP VARCHAR(255) NOT NULL,
            >_500 VARCHAR(255) NOT NULL,
            <_500 VARCHAR(255) NOT NULL,
            Season VARCHAR(255) NOT NULL,
            errors  NUMERIC(5,6), NOT NULL,
            z_score NUMERIC(5,6), NOT NULL



        )
        """



  """
        DROP TABLE IF EXISTS vendor_parts CASCADE 

        """,
        """
        DROP TABLE IF EXISTS vendors CASCADE 
        """,
        """
        DROP TABLE IF EXISTS parts CASCADE 
        """,
        """
        DROP TABLE IF EXISTS part_drawings CASCADE 
        """,
        """
        DROP TABLE IF EXISTS vendor_parts CASCADE 
        """
