use mgsv_server;

-- server_user table
CREATE TABLE IF NOT EXISTS server_user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    email VARCHAR(255)
    -- Add other user-related fields here
);

-- character table
CREATE TABLE IF NOT EXISTS player_character (
    character_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    custom_name VARCHAR(255),
    player_class INT,
    player_type INT,
    last_loadout INT,
    last_active INT,
    selected_bgm INT,
    _version_ BIGINT,
    FOREIGN KEY (user_id) REFERENCES server_user(id)
);

-- avatar table
CREATE TABLE IF NOT EXISTS avatar (
    avatar_id INT AUTO_INCREMENT PRIMARY KEY,
    avatar_index INT,
    character_id INT,
    accessory_flags INT,
    beard_length INT,
    beard_style INT,
    eyebrow_style INT,
    eyebrow_width INT,
    face_color INT,
    face_race INT,
    face_type INT,
    face_variation INT,
    gash_or_tattoo_variation INT,
    hair_color INT,
    hair_style INT,
    left_eye_brightness INT,
    left_eye_color INT,
    right_eye_brightness INT,
    right_eye_color INT,
    tattoo_color INT,
    voice INT,
    FOREIGN KEY (character_id) REFERENCES player_character(character_id)
);

-- motion_frame table
CREATE TABLE IF NOT EXISTS motion_frame (
    motion_frame_id INT AUTO_INCREMENT PRIMARY KEY,
    avatar_id INT,
    frame_value INT,
    FOREIGN KEY (avatar_id) REFERENCES avatar(avatar_id)
);

-- match table
CREATE TABLE IF NOT EXISTS match_info (
    match_id INT AUTO_INCREMENT PRIMARY KEY,
    character_id INT,
    auto_leave INT,
    briefing_time INT,
    host_comment INT,
    max_capacity INT,
    mission_slot_count INT,
    player_num INT,
    FOREIGN KEY (character_id) REFERENCES player_character(character_id)
);

-- mission_slot table
CREATE TABLE IF NOT EXISTS mission_slot (
    mission_slot_id INT AUTO_INCREMENT PRIMARY KEY,
    match_id INT,
    flags INT,
    map INT,
    night INT,
    rule INT,
    rush INT,
    ticket INT,
    duration INT,
    unique_character INT,
    weather INT,
    FOREIGN KEY (match_id) REFERENCES match_info(match_id)
);

-- preset_radio_rule table
CREATE TABLE IF NOT EXISTS preset_radio_rule (
    preset_radio_rule_id INT AUTO_INCREMENT PRIMARY KEY,
    character_id INT,
    preset_radio_id_list TEXT,
    FOREIGN KEY (character_id) REFERENCES player_character(character_id)
);

-- loadout table
CREATE TABLE IF NOT EXISTS loadout (
    loadout_id INT AUTO_INCREMENT PRIMARY KEY,
    character_id INT,
    custom_name VARCHAR(255),
    loadout_version BIGINT,
    FOREIGN KEY (character_id) REFERENCES player_character(character_id)
);

-- gear table
CREATE TABLE IF NOT EXISTS gear (
    gear_id INT AUTO_INCREMENT PRIMARY KEY,
    loadout_id INT,
    id INT,
    model BIGINT,
    color_list TEXT,
    FOREIGN KEY (loadout_id) REFERENCES loadout(loadout_id)
);

CREATE TABLE IF NOT EXISTS item (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    slot INT,
    loadout_id INT,
    FOREIGN KEY (loadout_id) REFERENCES loadout(loadout_id)
);

CREATE TABLE IF NOT EXISTS skill (
    skill_id INT PRIMARY KEY AUTO_INCREMENT,
    slot INT,
    loadout_id INT,
    FOREIGN KEY (loadout_id) REFERENCES loadout(loadout_id)
);

CREATE TABLE IF NOT EXISTS support_weapon (
    support_weapon_id INT PRIMARY KEY AUTO_INCREMENT,
    slot INT,
    loadout_id INT,
    FOREIGN KEY (loadout_id) REFERENCES loadout(loadout_id)
);

CREATE TABLE IF NOT EXISTS weapon (
    weapon_id INT PRIMARY KEY AUTO_INCREMENT,
    slot INT,
    loadout_id INT,
    FOREIGN KEY (loadout_id) REFERENCES loadout(loadout_id)
);

CREATE TABLE IF NOT EXISTS color (
    color_id INT PRIMARY KEY AUTO_INCREMENT,
    color_value INT,
    loadout_id INT,
    FOREIGN KEY (loadout_id) REFERENCES loadout(loadout_id)
);

-- weapon_part table (if applicable)
CREATE TABLE IF NOT EXISTS weapon_part (
    weapon_part_id INT AUTO_INCREMENT PRIMARY KEY,
    weapon_id INT,
    part_id INT,
    FOREIGN KEY (weapon_id) REFERENCES weapon(weapon_id) -- Replace 'weapon(weapon_id)' with the actual foreign key reference
);

-- permanent_unlock table (if user-specific)
CREATE TABLE IF NOT EXISTS permanent_unlock (
    permanent_unlock_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    unlock_value BIGINT,
    FOREIGN KEY (user_id) REFERENCES server_user(id)
);

