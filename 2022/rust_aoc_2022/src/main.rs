use rust_aoc_2022::read_file;
use std::env;

mod solutions;
use solutions::*;

macro_rules! solve {
    ($day:path, $input:expr) => {{
        use $day::*;
        solve($input);
    }};
}
fn main() {
    let args: Vec<String> = env::args().collect();
    let day: u8 = args[1].parse().unwrap();

    let input = read_file(day);

    match day {
        1 => solve!(day01, input),
        2 => solve!(day02, input),
        3 => solve!(day03, input),
        4 => solve!(day04, input),
        5 => solve!(day05, input),
        6 => solve!(day06, input),
        7 => solve!(day07, input),
        8 => solve!(day08, input),
        9 => solve!(day09, input),
        10 => solve!(day10, input),
        11 => solve!(day11, input),
        12 => solve!(day12, input),
        13 => solve!(day13, input),
        14 => solve!(day14, input),
        15 => solve!(day15, input),
        16 => solve!(day16, input),
        _ => {}
    }
}
