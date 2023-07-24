use std::collections::HashSet;

fn parse_line(l: &str) -> ((i32, i32), (i32, i32)) {
    let split_parts: [&str; 3] = ["Sensor at ", ": closest beacon is at ", ", "];
    let coord_parts: Vec<&str> = l
        .split(split_parts[0])
        .flat_map(|x| x.split(split_parts[1]))
        .flat_map(|x| x.split(split_parts[2]))
        .skip(1)
        .collect();

    let x1: i32 = coord_parts[0][2..].parse().unwrap();
    let y1: i32 = coord_parts[1][2..].parse().unwrap();
    let x2: i32 = coord_parts[2][2..].parse().unwrap();
    let y2: i32 = coord_parts[3][2..].parse().unwrap();

    ((x1, y1), (x2, y2))
}

fn dist(a: (i32, i32), b: (i32, i32)) -> i32 {
    (a.0 - b.0).abs() + (a.1 - b.1).abs()
}

fn range_to_consider(min_x: i32, max_x: i32, max_dist: i32) -> (i32, i32) {
    ((min_x - max_dist - 1), (max_x + max_dist + 2))
}

fn solve_pt_1(
    sensors: Vec<(i32, i32)>,
    beacons: Vec<(i32, i32)>,
    dists: Vec<i32>,
    r: (i32, i32),
) -> i32 {
    let beacon_hsh: HashSet<(i32, i32)> = HashSet::from_iter(beacons);
    let y = 2000000;
    let mut total = 0;

    for x in r.0..r.1 {
        let n_to_check = (x, y);
        if beacon_hsh.contains(&n_to_check) {
            continue;
        }
        for i in 0..sensors.len() {
            let n_dist = dist(sensors[i], n_to_check);
            let s_dist = dists[i];
            if n_dist <= s_dist {
                total += 1;
                break;
            }
        }
    }

    total
}

fn part_1(input: &String) -> i32 {
    let mut sensors: Vec<(i32, i32)> = vec![];
    let mut beacons: Vec<(i32, i32)> = vec![];

    for l in input.lines() {
        let (s, b) = parse_line(l);
        sensors.push(s);
        beacons.push(b);
    }
    let mut dists: Vec<i32> = vec![];
    for i in 0..sensors.len() {
        let (s, b) = (sensors[i], beacons[i]);
        dists.push(dist(s, b));
    }

    let max_dist = dists.iter().max().unwrap();

    let min_x = sensors.iter().map(|(a, _)| a).min().unwrap();
    let max_x = sensors.iter().map(|(a, _)| a).max().unwrap();

    let r = range_to_consider(*min_x, *max_x, *max_dist);

    let result = solve_pt_1(sensors, beacons, dists, r);
    result
}

fn calc_next_coord(c: (i32, i32), s: (i32, i32), s_dist: i32, max_x: i32) -> (i32, i32) {
    let x_dist = s.0 - c.0;
    let y_dist = (c.1 - s.1).abs();
    let x_jump;

    if x_dist > 0 {
        x_jump = x_dist + (s_dist - y_dist) + 1;
    } else {
        x_jump = (s_dist + x_dist + 1) - y_dist;
    }

    let new_x = c.0 + x_jump;
    if new_x > max_x {
        if c.1 == max_x {
            panic!("didn't find node in range");
        }
        return (0, c.1 + 1);
    }
    (new_x, c.1)
}

fn solve_pt_2(sensors: Vec<(i32, i32)>, dists: Vec<i32>) -> (i32, i32) {
    let max_x = 4000000;
    // let max_x = 20;

    let mut x = 0;
    let mut y = 0;
    'coord_loop: loop {
        let n_to_check = (x, y);

        // need to call calc_next_coord  with farthest in range sensor
        let mut farthest_sensor_index: Option<usize> = None;
        let mut farthest_sensor_dist = 0;
        for i in 0..sensors.len() {
            let n_dist = dist(sensors[i], n_to_check);

            let s_dist = dists[i];
            if n_dist == 0 {
                (x, y) = (x + s_dist, y);
                continue 'coord_loop;
            }

            if n_dist <= s_dist {
                if n_dist > farthest_sensor_dist {
                    farthest_sensor_dist = n_dist;
                    farthest_sensor_index = Some(i);
                }
            }
        }
        if let Some(i) = farthest_sensor_index {
            (x, y) = calc_next_coord(n_to_check, sensors[i], dists[i], max_x);
        } else {
            return n_to_check;
        }
    }
}

fn part_2(input: &String) -> u128 {
    let mut sensors: Vec<(i32, i32)> = vec![];
    let mut beacons: Vec<(i32, i32)> = vec![];

    for l in input.lines() {
        let (s, b) = parse_line(l);
        sensors.push(s);
        beacons.push(b);
    }
    let mut dists: Vec<i32> = vec![];
    for i in 0..sensors.len() {
        let (s, b) = (sensors[i], beacons[i]);
        dists.push(dist(s, b));
    }

    let coord = solve_pt_2(sensors, dists);

    let x = coord.0 as u128;
    let y = coord.1 as u128;

    x * 4000000 + y
}

pub fn solve(input: String) {
    // println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
