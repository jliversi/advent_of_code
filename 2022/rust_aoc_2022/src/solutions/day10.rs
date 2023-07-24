fn parse_command(l: &str) -> (i32, i32) {
    let parts: Vec<&str> = l.split_whitespace().collect();
    match parts[0] {
        "noop" => return (1, 0),
        "addx" => return (2, parts[1].parse().unwrap()),
        _ => panic!("bad command"),
    }
}

fn part_1(input: &String) -> i32 {
    const SIG_CYCLES: [i32; 6] = [20, 60, 100, 140, 180, 220];
    let mut measured_signals: Vec<i32> = vec![];

    let mut current_cycle = 0;
    let mut reg_value = 1;
    for l in input.lines() {
        let (num_cycles, reg_change) = parse_command(l);
        for _ in 0..num_cycles {
            current_cycle += 1;
            if SIG_CYCLES.contains(&current_cycle) {
                measured_signals.push(reg_value * current_cycle);
            }
        }
        reg_value = reg_value + reg_change;
    }
    measured_signals.iter().sum()
}

fn part_2(input: &String) {
    let mut current_cycle: i32 = 0;
    let mut reg_value: i32 = 1;
    let mut line_to_print = "".to_string();
    for l in input.lines() {
        let (num_cycles, reg_change) = parse_command(l);
        for _ in 0..num_cycles {
            let hor_pos = current_cycle % 40;
            if (reg_value - hor_pos).abs() < 2 {
                line_to_print.push('#');
            } else {
                line_to_print.push('.');
            }
            current_cycle += 1;
            if (current_cycle % 40) == 0 {
                println!("{}", line_to_print);
                line_to_print.clear();
            }
        }
        reg_value = reg_value + reg_change;
    }
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution:");
    part_2(&input);
}
