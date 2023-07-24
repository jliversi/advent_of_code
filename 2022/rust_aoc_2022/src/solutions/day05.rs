use itertools::Itertools;
use regex::Regex;

fn build_stacks(stack_str: &str) -> Vec<Vec<char>> {
    let stack_lines: Vec<&str> = stack_str.lines().collect();
    let num_stacks = (stack_lines.last().unwrap().len() + 1) / 4;
    let mut result: Vec<Vec<char>> = vec![Vec::new(); num_stacks];
    for l in stack_lines {
        let l_with_buffer = l.to_owned() + " ";
        for (i, (_, c, _, _)) in l_with_buffer.chars().tuples().enumerate() {
            if c == ' ' || c.is_numeric() {
                continue;
            }
            result[i].insert(0, c);
        }
    }
    result
}

fn parse_moves(moves_str: &str) -> Vec<(u32, u32, u32)> {
    let mut result = Vec::new();

    for l in moves_str.lines() {
        let alpha_rgx = Regex::new(r"[a-zA-Z ]+").unwrap();
        let nums: Vec<u32> = alpha_rgx
            .split(l)
            .map(|x| x.parse::<u32>().unwrap_or(0))
            .collect();

        result.push((nums[1], nums[2], nums[3]));
    }

    result
}

fn execute_move_pt1(
    move_instruction: (u32, u32, u32),
    mut stacks: Vec<Vec<char>>,
) -> Vec<Vec<char>> {
    let (num_to_move, stack1_idx, stack2_idx) = move_instruction;
    for _ in 0..num_to_move {
        let ele = stacks[stack1_idx as usize - 1].pop().unwrap();
        stacks[stack2_idx as usize - 1].push(ele);
    }
    stacks
}

fn execute_move_pt2(
    move_instruction: (u32, u32, u32),
    mut stacks: Vec<Vec<char>>,
) -> Vec<Vec<char>> {
    let (num_to_move, stack1_idx, stack2_idx) = move_instruction;

    let current_stack_size = stacks[stack1_idx as usize - 1].len();
    let mut eles_to_move =
        stacks[stack1_idx as usize - 1].split_off(current_stack_size - (num_to_move as usize));
    stacks[stack2_idx as usize - 1].append(&mut eles_to_move);

    stacks
}

fn read_stacks(stacks: Vec<Vec<char>>) -> String {
    stacks.iter().map(|s| s.last().unwrap()).join("")
}

fn part_1(input: &String) -> String {
    let input_parts: Vec<&str> = input.split("\n\n").collect();
    let stack_input = input_parts[0];
    let mut stacks = build_stacks(stack_input);

    let moves_input = input_parts[1];
    let moves = parse_moves(moves_input);

    for m in moves {
        stacks = execute_move_pt1(m, stacks);
    }
    read_stacks(stacks)
}

fn part_2(input: &String) -> String {
    let input_parts: Vec<&str> = input.split("\n\n").collect();
    let stack_input = input_parts[0];
    let mut stacks = build_stacks(stack_input);

    let moves_input = input_parts[1];
    let moves = parse_moves(moves_input);

    for m in moves {
        stacks = execute_move_pt2(m, stacks);
    }
    read_stacks(stacks)
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
