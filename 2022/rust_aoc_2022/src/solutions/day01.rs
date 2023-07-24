fn part_1(input: &String) -> i32 {
    let elves = input.split("\n\n");
    let largest_elf = elves
        .map(|elf| elf.lines().map(|x| x.parse::<i32>().unwrap()).sum::<i32>())
        .max();
    largest_elf.unwrap()
}

fn part_2(input: &String) -> i32 {
    let mut elves = input
        .split("\n\n")
        .map(|elf| elf.lines().map(|x| x.parse::<i32>().unwrap()).sum::<i32>())
        .collect::<Vec<i32>>();
    elves.sort();
    elves.iter().rev().take(3).sum()
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
