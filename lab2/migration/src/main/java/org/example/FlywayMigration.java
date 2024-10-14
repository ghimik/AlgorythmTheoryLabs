package org.example;

import org.flywaydb.core.Flyway;

public class FlywayMigration {

    public static void migrate() {
        Flyway flyway = Flyway.configure()
                .dataSource("jdbc:postgresql://0.0.0.0:5432/lab3",
                        "postgres", "admin")
                .locations("filesystem:src/main/resources/db/migration")
                .load();

        flyway.migrate();
    }

}
