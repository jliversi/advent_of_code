#[derive(Debug)]
enum Opperand {
    Old,
    Val(u64),
}

#[derive(Debug)]
enum Opp {
    Multiply(Opperand),
    Add(Opperand),
}

#[derive(Debug)]
struct Monkey {
    items: Vec<u64>,
    operation: Opp,
    divisor: u64,
    true_target: usize,
    false_target: usize,
    items_inspected: u64,
}

impl Monkey {
    fn new(
        items: Vec<u64>,
        operation: Opp,
        divisor: u64,
        true_target: usize,
        false_target: usize,
    ) -> Monkey {
        return Monkey {
            items,
            operation,
            divisor,
            true_target,
            false_target,
            items_inspected: 0,
        };
    }

    fn inspect_item_1(&mut self) -> u64 {
        match self.items.pop() {
            Some(item) => match &self.operation {
                Opp::Add(o) => match o {
                    Opperand::Old => (item + item) / 3,
                    Opperand::Val(v) => (item + v) / 3,
                },
                Opp::Multiply(o) => match o {
                    Opperand::Old => (item * item) / 3,
                    Opperand::Val(v) => (item * v) / 3,
                },
            },
            None => 0,
        }
    }

    fn inspect_item_2(&mut self, div: u64) -> u64 {
        match self.items.pop() {
            Some(item) => match &self.operation {
                Opp::Add(o) => match o {
                    Opperand::Old => (item + item) % div,
                    Opperand::Val(v) => (item + v) % div,
                },
                Opp::Multiply(o) => match o {
                    Opperand::Old => (item % div) * (item % div),
                    Opperand::Val(v) => (item % div) * v,
                },
            },
            None => 0,
        }
    }

    fn new_monkey_idx(&self, item: u64) -> usize {
        if (item % self.divisor) == 0 {
            self.true_target
        } else {
            self.false_target
        }
    }
}

fn build_monkeys(input: &String) -> Vec<Monkey> {
    let mut monkeys: Vec<Monkey> = vec![];
    for m_string in input.split("\n\n") {
        let lines: Vec<&str> = m_string.lines().map(|x| x.trim()).collect();
        // Items
        let mut items: Vec<u64> = vec![];
        for item in lines[1].split_whitespace().skip(2) {
            if item.chars().last() == Some(',') {
                items.push(item[0..item.len() - 1].parse().unwrap());
            } else {
                items.push(item.parse().unwrap());
            }
        }
        // Operation
        let op_parts: Vec<&str> = lines[2].split_whitespace().collect();
        let operation = match op_parts[4] {
            "+" => match op_parts[5].parse() {
                Ok(val) => Opp::Add(Opperand::Val(val)),
                Err(_) => Opp::Add(Opperand::Old),
            },
            "*" => match op_parts[5].parse() {
                Ok(val) => Opp::Multiply(Opperand::Val(val)),
                Err(_) => Opp::Multiply(Opperand::Old),
            },
            _ => panic!("unrecognized opp"),
        };
        // Divisor
        let divisor: u64 = lines[3].split_whitespace().last().unwrap().parse().unwrap();
        // True & False Targets
        let true_target: usize = lines[4].split_whitespace().last().unwrap().parse().unwrap();
        let false_target: usize = lines[5].split_whitespace().last().unwrap().parse().unwrap();

        let new_monkey = Monkey::new(items, operation, divisor, true_target, false_target);
        monkeys.push(new_monkey);
    }
    monkeys
}

fn run_round_1(monkeys: &mut Vec<Monkey>) {
    for i in 0..monkeys.len() {
        let mut items_to_insert: Vec<Vec<u64>> = vec![vec![]; monkeys.len()];
        let mut m = &mut monkeys[i];

        while !m.items.is_empty() {
            let next_item = m.inspect_item_1();
            m.items_inspected += 1;
            let next_monkey_idx = m.new_monkey_idx(next_item);
            items_to_insert[next_monkey_idx].push(next_item);
        }

        for (i, items) in items_to_insert.iter().enumerate() {
            for item in items.iter().rev() {
                monkeys[i].items.push(*item);
            }
        }
    }
}

fn run_round_2(monkeys: &mut Vec<Monkey>, div: u64) {
    for i in 0..monkeys.len() {
        let mut items_to_insert: Vec<Vec<u64>> = vec![vec![]; monkeys.len()];
        let mut m = &mut monkeys[i];

        while !m.items.is_empty() {
            let next_item = m.inspect_item_2(div);
            m.items_inspected += 1;
            let next_monkey_idx = m.new_monkey_idx(next_item);
            items_to_insert[next_monkey_idx].push(next_item);
        }

        for (i, items) in items_to_insert.iter().enumerate() {
            for item in items.iter().rev() {
                monkeys[i].items.push(*item);
            }
        }
    }
}

fn part_1(input: &String) -> u64 {
    let mut monkeys = build_monkeys(input);
    for _ in 0..20 {
        run_round_1(&mut monkeys);
    }

    let mut inspect_counts: Vec<u64> = monkeys.iter().map(|m| m.items_inspected).collect();
    inspect_counts.sort();
    inspect_counts.reverse();

    inspect_counts[0..2].iter().product::<u64>()
}

fn part_2(input: &String) -> u64 {
    let mut monkeys = build_monkeys(input);

    let div = monkeys.iter().map(|m| m.divisor).product();

    for _ in 0..10000 {
        run_round_2(&mut monkeys, div);
    }

    let mut inspect_counts: Vec<u64> = monkeys.iter().map(|m| m.items_inspected).collect();
    inspect_counts.sort();
    inspect_counts.reverse();

    inspect_counts[0..2].iter().product::<u64>()
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
