/*
X IS HORIZONTAL VALUE
Y IS VERTICAL VALUE (or height)
*/

fn verticies_to_coords(x1: usize, y1: usize, x2: usize, y2: usize) -> Vec<(usize, usize)> {
    let mut result = Vec::from([]);

    // Moving vertical
    if x1 == x2 {
        let mut new_y = y1;
        // Moving up
        if y1 < y2 {
            while new_y < y2 {
                new_y += 1;
                result.push((x1, new_y));
            }
        }
        // Moving down
        if y1 > y2 {
            while new_y > y2 {
                new_y -= 1;
                result.push((x1, new_y));
            }
        }
    }

    // Moving horizontal
    if y1 == y2 {
        let mut new_x = x1;
        // Moving right
        if x1 < x2 {
            while new_x < x2 {
                new_x += 1;
                result.push((new_x, y1));
            }
        }
        // Moving left
        if x1 > x2 {
            while new_x > x2 {
                new_x -= 1;
                result.push((new_x, y1));
            }
        }
    }
    result
}

fn line_to_coords(l: &str) -> Vec<(usize, usize)> {
    let mut verticies = vec![];
    for coord_pair in l.split(" -> ") {
        let coords: Vec<&str> = coord_pair.split(",").collect();
        let x = coords[0];
        let y = coords[1];
        let coord: (usize, usize) = (x.parse().unwrap(), y.parse().unwrap());
        verticies.push(coord);
    }

    let mut result = vec![];

    result.push(verticies[0]);
    for i in 0..(verticies.len() - 1) {
        let (c1, c2) = (verticies[i], verticies[i + 1]);
        let (x1, y1) = c1;
        let (x2, y2) = c2;

        let mut new_coords = verticies_to_coords(x1, y1, x2, y2);
        result.append(&mut new_coords);
    }

    result
}

fn find_max_coords(all_coords: &Vec<(usize, usize)>) -> (usize, usize) {
    let (mut max_x, mut max_y): (usize, usize) = (500, 0);

    for &c in all_coords {
        let (x, y) = c;
        if x > max_x {
            max_x = x;
        }
        if y > max_y {
            max_y = y;
        }
    }

    (max_x, max_y)
}

fn build_grid_1(input: &String) -> Vec<Vec<bool>> {
    let wall_coords = input.lines().map(|l| line_to_coords(l)).flatten().collect();

    let (max_x, max_y) = find_max_coords(&wall_coords);

    let mut result = vec![vec![false; max_y + 1]; max_x + 1];

    for (x, y) in wall_coords {
        result[x][y] = true;
    }

    result
}

fn next_sand_pos(sand_x: usize, sand_y: usize, grid: &Vec<Vec<bool>>) -> Option<(usize, usize)> {
    let (new_x, new_y) = (sand_x, sand_y + 1);
    if !grid[new_x][new_y] {
        return Some((new_x, new_y));
    }

    let (new_x, new_y) = (sand_x - 1, sand_y + 1);
    if !grid[new_x][new_y] {
        return Some((new_x, new_y));
    }

    let (new_x, new_y) = (sand_x + 1, sand_y + 1);
    if !grid[new_x][new_y] {
        return Some((new_x, new_y));
    }

    None
}

fn add_sand(grid: &mut Vec<Vec<bool>>) -> Option<(usize, usize)> {
    let max_y = grid[0].len() - 1;
    let (mut sand_x, mut sand_y) = (500, 0);

    while let Some((new_x, new_y)) = next_sand_pos(sand_x, sand_y, &grid) {
        sand_x = new_x;
        sand_y = new_y;

        if new_y == max_y {
            return None;
        }
    }

    grid[sand_x][sand_y] = true;

    if (sand_x, sand_y) == (500, 0) {
        return None;
    }
    Some((sand_x, sand_y))
}

fn part_1(input: &String) -> i32 {
    let mut grid = build_grid_1(input);

    let mut sand_count = 0;
    while let Some((_, _)) = add_sand(&mut grid) {
        sand_count += 1;
    }

    sand_count
}

fn build_grid_2(input: &String) -> Vec<Vec<bool>> {
    let wall_coords = input.lines().map(|l| line_to_coords(l)).flatten().collect();

    let (max_x, max_y) = find_max_coords(&wall_coords);

    let mut result = vec![vec![false; max_y + 1]; max_x + max_y + 1];

    for (x, y) in wall_coords {
        result[x][y] = true;
    }

    for i in 0..result.len() {
        result[i].push(false);
        result[i].push(true);
    }

    result
}

fn part_2(input: &String) -> i32 {
    let mut grid = build_grid_2(input);

    let mut sand_count = 0;
    while let Some((_, _)) = add_sand(&mut grid) {
        sand_count += 1;
    }

    sand_count + 1
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
