struct AssignmentRange(i32, i32);

fn line_to_range(l: &str) -> (AssignmentRange, AssignmentRange) {
    let nums: Vec<i32> = l
        .split(|c: char| !c.is_numeric())
        .map(|x| x.parse::<i32>().unwrap())
        .collect();
    (
        AssignmentRange(nums[0], nums[1]),
        AssignmentRange(nums[2], nums[3]),
    )
}

fn ranges_full_overlap((r1, r2): (AssignmentRange, AssignmentRange)) -> bool {
    let r1_in_r2 = r1.0 <= r2.0 && r2.1 <= r1.1;
    let r2_in_r1 = r2.0 <= r1.0 && r1.1 <= r2.1;
    r1_in_r2 || r2_in_r1
}

fn part_1(input: &String) -> i32 {
    let mut total = 0;
    for l in input.lines() {
        if ranges_full_overlap(line_to_range(l)) {
            total += 1
        }
    }
    total
}

fn ranges_overlap((r1, r2): (AssignmentRange, AssignmentRange)) -> bool {
    let r1_before_r2 = r1.1 < r2.0;
    let r2_before_r1 = r2.1 < r1.0;
    !(r1_before_r2 || r2_before_r1)
}

fn part_2(input: &String) -> i32 {
    let mut total = 0;
    for l in input.lines() {
        if ranges_overlap(line_to_range(l)) {
            total += 1
        }
    }
    total
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
