use itertools::Itertools;

fn find_packet_marker(input: &str) -> Option<usize> {
    for (i, (a, b, c, d)) in input.chars().tuple_windows().enumerate() {
        dbg!(i, (a, b, c, d));
        if !(a == b || a == c || a == d || b == c || b == d || c == d) {
            return Some(i + 4);
        }
    }
    None
}

fn find_message_marker(input: &str) -> Option<usize> {
    let input_len = input.chars().count();

    for e in 14..input_len {
        let s = e - 14;
        let window = &input[s..e];
        let unique_chars = window.chars().unique().count();
        if unique_chars == 14 {
            return Some(e);
        }
    }

    None
}

fn part_1(input: &String) -> usize {
    find_packet_marker(input).unwrap()
}

fn part_2(input: &String) -> usize {
    find_message_marker(input).unwrap()
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
