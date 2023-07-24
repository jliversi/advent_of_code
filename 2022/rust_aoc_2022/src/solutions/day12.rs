fn build_grid(input: &String) -> (Vec<Vec<u32>>, (usize, usize), (usize, usize)) {
    let mut start: (usize, usize) = (0, 0);
    let mut end: (usize, usize) = (0, 0);

    let mut grid = vec![];
    for (i, l) in input.lines().enumerate() {
        let mut row = vec![];
        for (j, c) in l.chars().enumerate() {
            match c {
                'S' => {
                    start = (i, j);
                    row.push(10);
                }
                'E' => {
                    end = (i, j);
                    row.push(35);
                }
                _ => row.push(c.to_digit(36).unwrap()),
            }
        }
        grid.push(row);
    }

    (grid, start, end)
}

fn neighbors_1(coord: (usize, usize), grid: &Vec<Vec<u32>>) -> Vec<(usize, usize)> {
    let mut result = vec![];
    let (x, y) = coord;
    let val = grid[x][y];
    let x_len = grid.len();
    let y_len = grid[0].len();

    let t_n = (
        match x.checked_sub(1) {
            Some(n) => n,
            None => std::usize::MAX,
        },
        y,
    );
    let l_n = (
        x,
        match y.checked_sub(1) {
            Some(n) => n,
            None => std::usize::MAX,
        },
    );
    let b_n = (x + 1, y);
    let r_n = (x, y + 1);

    for nbr in [t_n, r_n, b_n, l_n] {
        let (nx, ny) = nbr;

        if nx < x_len && ny < y_len && val >= (grid[nx][ny] - 1) {
            result.push(nbr);
        }
    }
    result
}

fn dijkstra_1(grid: Vec<Vec<u32>>, start: (usize, usize), end: (usize, usize)) -> u32 {
    let (s_x, s_y) = start;
    let (e_x, e_y) = end;
    let x_len = grid.len();
    let y_len = grid[0].len();

    let mut visited_grid = vec![vec![false; y_len]; x_len];
    let mut distance_grid = vec![vec![std::u32::MAX; y_len]; x_len];
    distance_grid[s_x][s_y] = 0;

    let mut current_coord = start;

    while !visited_grid[e_x][e_y] {
        let (c_x, c_y) = current_coord;
        let cur_dist = distance_grid[c_x][c_y];
        let nbrs = neighbors_1(current_coord, &grid);
        for nbr in nbrs {
            let (n_x, n_y) = nbr;
            if visited_grid[n_x][n_y] {
                continue;
            } else {
                let nbr_dist = distance_grid[n_x][n_y];
                if nbr_dist > cur_dist + 1 {
                    distance_grid[n_x][n_y] = cur_dist + 1;
                }
            }
        }
        visited_grid[c_x][c_y] = true;

        // Find next current
        let mut cur_min = std::u32::MAX;
        for i in 0..x_len {
            for j in 0..y_len {
                if visited_grid[i][j] {
                    continue;
                } else if distance_grid[i][j] < cur_min {
                    cur_min = distance_grid[i][j];
                    current_coord = (i, j);
                }
            }
        }
    }

    distance_grid[e_x][e_y]
}

fn part_1(input: &String) -> u32 {
    let (grid, start, end) = build_grid(input);
    let result = dijkstra_1(grid, start, end);
    result
}

fn neighbors_2(coord: (usize, usize), grid: &Vec<Vec<u32>>) -> Vec<(usize, usize)> {
    let mut result = vec![];
    let (x, y) = coord;
    let val = grid[x][y];
    let x_len = grid.len();
    let y_len = grid[0].len();

    let t_n = (
        match x.checked_sub(1) {
            Some(n) => n,
            None => std::usize::MAX,
        },
        y,
    );
    let l_n = (
        x,
        match y.checked_sub(1) {
            Some(n) => n,
            None => std::usize::MAX,
        },
    );
    let b_n = (x + 1, y);
    let r_n = (x, y + 1);

    for nbr in [t_n, r_n, b_n, l_n] {
        let (nx, ny) = nbr;

        if nx < x_len && ny < y_len && (grid[nx][ny] >= val - 1) {
            result.push(nbr);
        }
    }
    result
}

fn part_2(input: &String) -> u32 {
    let (grid, _, end) = build_grid(input);

    let result = dijkstra_2(grid, end);
    result
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}

fn dijkstra_2(grid: Vec<Vec<u32>>, start: (usize, usize)) -> u32 {
    let (s_x, s_y) = start;
    let x_len = grid.len();
    let y_len = grid[0].len();

    let mut visited_grid = vec![vec![false; y_len]; x_len];
    let mut distance_grid = vec![vec![std::u32::MAX; y_len]; x_len];
    distance_grid[s_x][s_y] = 0;

    let mut current_coord = start;

    loop {
        let (c_x, c_y) = current_coord;
        let cur_dist = distance_grid[c_x][c_y];
        let nbrs = neighbors_2(current_coord, &grid);
        for nbr in nbrs {
            let (n_x, n_y) = nbr;
            if visited_grid[n_x][n_y] {
                continue;
            } else {
                let nbr_dist = distance_grid[n_x][n_y];
                if nbr_dist > cur_dist + 1 {
                    distance_grid[n_x][n_y] = cur_dist + 1;
                }
            }
        }
        visited_grid[c_x][c_y] = true;
        if grid[c_x][c_y] == 10 {
            return distance_grid[c_x][c_y];
        }

        // Find next current
        let mut cur_min = std::u32::MAX;
        for i in 0..x_len {
            for j in 0..y_len {
                if visited_grid[i][j] {
                    continue;
                } else if distance_grid[i][j] < cur_min {
                    cur_min = distance_grid[i][j];
                    current_coord = (i, j);
                }
            }
        }
    }
}
