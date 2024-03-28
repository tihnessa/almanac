CREATE TABLE campaigns(
    id TEXT NOT NULL UNIQUE PRIMARY KEY,
    title TEXT NOT NULL,
    ruleset TEXT NOT NULL,
    version TEXT,
    setting TEXT,
    started TEXT,
    finished TEXT,
    last_update TEXT,
    status TEXT NOT NULL CHECK (status IN ('Planning', 'Active', 'On hold', 'Finished', 'Abandoned'))
);

CREATE TABLE players(
    id TEXT NOT NULL UNIQUE PRIMARY KEY,
    name TEXT NOT NULL,
    contact_number TEXT,
    email TEXT,
    preferred_contact TEXT,
    status TEXT NOT NULL CHECK (status IN('Active', 'Inactive', 'Uncontactable'))
);

CREATE TABLE rulesets(
    id TEXT NOT NULL UNIQUE PRIMARY KEY,
    title TEXT NOT NULL
)
