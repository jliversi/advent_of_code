use std::collections::HashSet;

fn update_tail_pos(head_pos: &(i32, i32), tail_pos: (i32, i32)) -> (i32, i32) {
    if ((head_pos.0 - tail_pos.0).abs() < 2) && ((head_pos.1 - tail_pos.1).abs() < 2) {
        return tail_pos;
    }

    if head_pos.0 == tail_pos.0 {
        if (head_pos.1 - tail_pos.1).abs() < 2 {
            return tail_pos;
        } else if tail_pos.1 > head_pos.1 {
            return (tail_pos.0, tail_pos.1 - 1);
        } else {
            return (tail_pos.0, tail_pos.1 + 1);
        }
    }
    if head_pos.1 == tail_pos.1 {
        if (head_pos.0 - tail_pos.0).abs() < 2 {
            return tail_pos;
        } else if tail_pos.0 > head_pos.0 {
            return (tail_pos.0 - 1, tail_pos.1);
        } else {
            return (tail_pos.0 + 1, tail_pos.1);
        }
    }
    let tx;
    if tail_pos.0 > head_pos.0 {
        tx = tail_pos.0 - 1;
    } else {
        tx = tail_pos.0 + 1;
    }
    let ty;
    if tail_pos.1 > head_pos.1 {
        ty = tail_pos.1 - 1;
    } else {
        ty = tail_pos.1 + 1;
    }

    (tx, ty)
}

fn update_head_pos(head_pos: (i32, i32), dir: &str) -> (i32, i32) {
    match dir {
        "R" => return (head_pos.0 + 1, head_pos.1),
        "L" => return (head_pos.0 - 1, head_pos.1),
        "U" => return (head_pos.0, head_pos.1 + 1),
        "D" => return (head_pos.0, head_pos.1 - 1),
        _ => panic!("unrecognized dir"),
    }
}

fn part_1(input: &String) -> usize {
    let mut head_pos = (0, 0);
    let mut tail_pos = (0, 0);
    let mut tail_positions: HashSet<(i32, i32)> = HashSet::from([(0, 0)]);
    for line in input.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        let dir = split[0];
        let times: i32 = split[1].parse().unwrap();
        for _ in 0..times {
            head_pos = update_head_pos(head_pos, dir);
            tail_pos = update_tail_pos(&head_pos, tail_pos);
            tail_positions.insert(tail_pos);
        }
    }
    tail_positions.len()
}

fn part_2(input: &String) -> usize {
    let mut positions: [(i32, i32); 10] = [(0, 0); 10];
    let mut tail_positions: HashSet<(i32, i32)> = HashSet::from([(0, 0)]);
    for line in input.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        let dir = split[0];
        let times: i32 = split[1].parse().unwrap();
        for _ in 0..times {
            positions[0] = update_head_pos(positions[0], dir);
            for i in 1..10 {
                positions[i] = update_tail_pos(&positions[i - 1], positions[i])
            }
            tail_positions.insert(positions[9]);
        }
    }
    tail_positions.len()
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
