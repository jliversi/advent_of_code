use itertools::Itertools;

const ALPHA: &str = "@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

fn char_priority(c: char) -> usize {
    ALPHA.find(c).unwrap()
}

fn part_1(input: &String) -> usize {
    let mut total = 0;

    for sack in input.lines() {
        let mid = sack.len() / 2;
        let left = &sack[0..mid];
        let right = &sack[mid..];
        for c in left.chars() {
            if right.contains(c) {
                total += char_priority(c);
                break;
            }
        }
    }
    total
}

fn part_2(input: &String) -> usize {
    let mut total = 0;

    for (l1, l2, l3) in input.lines().tuples() {
        for c in l1.chars() {
            if l2.contains(c) && l3.contains(c) {
                total += char_priority(c);
                break;
            }
        }
    }
    total
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
