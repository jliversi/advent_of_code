#[derive(PartialEq)]
enum Choice {
    Rock,
    Paper,
    Scissors,
}

fn find_loser(choice1: &Choice) -> Choice {
    match choice1 {
        Choice::Rock => Choice::Scissors,
        Choice::Paper => Choice::Rock,
        Choice::Scissors => Choice::Paper,
    }
}

fn find_winner(choice1: &Choice) -> Choice {
    match choice1 {
        Choice::Rock => Choice::Paper,
        Choice::Paper => Choice::Scissors,
        Choice::Scissors => Choice::Rock,
    }
}

fn find_tie(choice1: &Choice) -> Choice {
    match choice1 {
        Choice::Rock => Choice::Rock,
        Choice::Paper => Choice::Paper,
        Choice::Scissors => Choice::Scissors,
    }
}

fn convert_elf_throw(input: &str) -> Choice {
    match input {
        "A" => Choice::Rock,
        "B" => Choice::Paper,
        "C" => Choice::Scissors,
        _ => panic!("Input could not be mapped"),
    }
}

fn convert_pt1_throw(input: &str) -> Choice {
    match input {
        "X" => Choice::Rock,
        "Y" => Choice::Paper,
        "Z" => Choice::Scissors,
        _ => panic!("Input could not be mapped"),
    }
}

fn convert_pt2_throw(opp_choice: &Choice, input: &str) -> Choice {
    match input {
        "X" => find_loser(opp_choice),
        "Y" => find_tie(opp_choice),
        "Z" => find_winner(opp_choice),
        _ => panic!("Input could not be mapped"),
    }
}

fn round_pts(opp_choice: Choice, my_choice: Choice) -> i32 {
    if opp_choice == my_choice {
        3
    } else if my_choice == find_winner(&opp_choice) {
        6
    } else {
        0
    }
}

fn choice_pts(choice: &Choice) -> i32 {
    match choice {
        Choice::Rock => 1,
        Choice::Paper => 2,
        Choice::Scissors => 3,
    }
}

fn part_1(input: &String) -> i32 {
    let mut total: i32 = 0;
    for line in input.lines() {
        let opp = convert_elf_throw(&line[0..1]);
        let me = convert_pt1_throw(&line[2..]);
        total += choice_pts(&me);
        total += round_pts(opp, me);
    }
    total
}

fn part_2(input: &String) -> i32 {
    let mut total: i32 = 0;
    for line in input.lines() {
        let opp = convert_elf_throw(&line[0..1]);
        let me = convert_pt2_throw(&opp, &line[2..]);
        total += choice_pts(&me);
        total += round_pts(opp, me);
    }
    total
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
