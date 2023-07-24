fn build_rows(input: &String) -> Vec<Vec<u8>> {
    let mut result: Vec<Vec<u8>> = vec![];
    for l in input.lines() {
        let mut row: Vec<u8> = vec![];
        for c in l.chars() {
            row.push(c.to_digit(10).unwrap() as u8);
        }
        result.push(row);
    }
    result
}

fn build_cols(rows: &Vec<Vec<u8>>) -> Vec<Vec<u8>> {
    (0..rows[0].len())
        .map(|i| {
            rows.iter()
                .map(|row| row.iter().nth(i).unwrap().clone())
                .collect()
        })
        .collect::<Vec<Vec<u8>>>()
}

fn tree_visible(rows: &Vec<Vec<u8>>, cols: &Vec<Vec<u8>>, x: usize, y: usize) -> bool {
    let tree_value = rows[x][y];

    let row = &rows[x];
    let visible_left = (0..y).all(|i| row[i] < tree_value);
    let visible_right = (y + 1..row.len()).all(|i| row[i] < tree_value);

    let col = &cols[y];
    let visible_above = (0..x).all(|i| col[i] < tree_value);
    let visible_below = (x + 1..col.len()).all(|i| col[i] < tree_value);

    visible_left || visible_right || visible_above || visible_below
}

fn part_1(input: &String) -> i32 {
    let rows = build_rows(&input);
    let cols = build_cols(&rows);

    let mut total_visible = 0;

    for i in 0..rows.len() {
        for j in 0..cols.len() {
            if tree_visible(&rows, &cols, i, j) {
                total_visible += 1;
            }
        }
    }

    total_visible
}

fn scenic_score(rows: &Vec<Vec<u8>>, cols: &Vec<Vec<u8>>, x: usize, y: usize) -> i32 {
    let tree_value = rows[x][y];

    let row = &rows[x];

    let mut score_left = 0;
    for i in (0..y).rev() {
        score_left += 1;
        if row[i] >= tree_value {
            break;
        }
    }

    let mut score_right = 0;
    for i in y + 1..row.len() {
        score_right += 1;
        if row[i] >= tree_value {
            break;
        }
    }

    let col = &cols[y];
    let mut score_above = 0;
    for i in (0..x).rev() {
        score_above += 1;
        if col[i] >= tree_value {
            break;
        }
    }

    let mut score_below = 0;
    for i in x + 1..col.len() {
        score_below += 1;
        if col[i] >= tree_value {
            break;
        }
    }

    score_left * score_right * score_above * score_below
}

fn part_2(input: &String) -> i32 {
    let rows = build_rows(&input);
    let cols = build_cols(&rows);

    let mut best_score = 0;
    for i in 0..rows.len() {
        for j in 0..cols.len() {
            let score = scenic_score(&rows, &cols, i, j);
            if score > best_score {
                best_score = score;
            }
        }
    }
    best_score
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
