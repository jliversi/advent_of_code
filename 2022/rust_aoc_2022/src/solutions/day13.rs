use std::cell::RefCell;
use std::fmt;
use std::rc::Rc;

use itertools::Itertools;
use std::cmp::Ordering;

struct SignalNode {
    value: i32,
    children: Vec<Rc<RefCell<SignalNode>>>,
    parent: Option<Rc<RefCell<SignalNode>>>,
    is_container: bool,
}

impl SignalNode {
    pub fn new(is_container: bool, value: i32) -> SignalNode {
        return SignalNode {
            value,
            children: vec![],
            parent: None,
            is_container,
        };
    }

    pub fn add_child(&mut self, new_node: Rc<RefCell<SignalNode>>) {
        self.children.push(new_node);
    }
}

impl fmt::Debug for SignalNode {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("SignalNode")
            .field("is_container", &self.is_container)
            .field("value", &self.value)
            .field("# children", &self.children.len())
            .finish()
    }
}

fn parse_line(l: &str) -> Rc<RefCell<SignalNode>> {
    let mut num_str = "".to_string();

    let root = Rc::new(RefCell::new(SignalNode::new(true, -1)));

    let mut current_node = Rc::clone(&root);

    for c in l.chars().skip(1).take(l.len() - 2) {
        if c.is_numeric() {
            num_str.push(c);
        } else {
            match c {
                ',' => {
                    if num_str.len() > 0 {
                        let value = num_str.parse().unwrap();
                        num_str.clear();

                        let new_node = Rc::new(RefCell::new(SignalNode::new(false, value)));
                        current_node.borrow_mut().add_child(Rc::clone(&new_node));
                        new_node.borrow_mut().parent = Some(Rc::clone(&current_node));
                    }
                }
                '[' => {
                    let new_node = Rc::new(RefCell::new(SignalNode::new(true, -1)));
                    current_node.borrow_mut().add_child(Rc::clone(&new_node));
                    new_node.borrow_mut().parent = Some(Rc::clone(&current_node));
                    current_node = Rc::clone(&new_node);
                }
                ']' => {
                    if num_str.len() > 0 {
                        let value = num_str.parse().unwrap();
                        num_str.clear();

                        let new_node = Rc::new(RefCell::new(SignalNode::new(false, value)));
                        current_node.borrow_mut().add_child(Rc::clone(&new_node));
                        new_node.borrow_mut().parent = Some(Rc::clone(&current_node));
                    }
                    let current_clone = Rc::clone(&current_node);
                    current_node = Rc::clone(current_clone.borrow().parent.as_ref().unwrap());
                }
                _ => panic!("unrecognized char"),
            }
        }
    }
    if num_str.len() > 0 {
        let value = num_str.parse().unwrap();
        num_str.clear();

        let new_node = Rc::new(RefCell::new(SignalNode::new(false, value)));
        current_node.borrow_mut().add_child(Rc::clone(&new_node));
        new_node.borrow_mut().parent = Some(Rc::clone(&current_node));
    }

    root
}

fn spaceship(a: i32, b: i32) -> Ordering {
    if a < b {
        return Ordering::Less;
    } else if a > b {
        return Ordering::Greater;
    } else {
        return Ordering::Equal;
    }
}

fn in_order(s1: Rc<RefCell<SignalNode>>, s2: Rc<RefCell<SignalNode>>) -> Ordering {
    let node1 = s1.borrow();
    let node2 = s2.borrow();

    // Neither is container
    if !node1.is_container && !node2.is_container {
        return spaceship(node1.value, node2.value);
    }

    // Both are containers
    if node1.is_container && node2.is_container {
        let mut children_checked = 0;
        for i in 0..node1.children.len() {
            if i >= node2.children.len() {
                return Ordering::Greater;
            }
            let tmp_result = in_order(Rc::clone(&node1.children[i]), Rc::clone(&node2.children[i]));
            if tmp_result != Ordering::Equal {
                return tmp_result;
            }
            children_checked += 1;
        }
        if children_checked == node2.children.len() {
            return Ordering::Equal;
        } else {
            return Ordering::Less;
        }
    }

    // Left is container
    if node1.is_container {
        let temp_right = Rc::new(RefCell::new(SignalNode::new(true, -1)));
        let right_child = Rc::new(RefCell::new(SignalNode::new(false, node2.value)));
        temp_right.borrow_mut().add_child(Rc::clone(&right_child));
        right_child.borrow_mut().parent = Some(Rc::clone(&temp_right));

        return in_order(Rc::clone(&s1), temp_right);
    }

    // Right is container
    let temp_left = Rc::new(RefCell::new(SignalNode::new(true, -1)));
    let left_child = Rc::new(RefCell::new(SignalNode::new(false, node1.value)));
    temp_left.borrow_mut().add_child(Rc::clone(&left_child));
    left_child.borrow_mut().parent = Some(Rc::clone(&temp_left));
    return in_order(temp_left, Rc::clone(&s2));
}

fn part_1(input: &String) -> i32 {
    let mut results: Vec<Ordering> = vec![];
    for trio in &input.lines().chunks(3) {
        let lines: Vec<&str> = trio.collect();
        let n1 = parse_line(lines[0]);
        let n2 = parse_line(lines[1]);
        let result = in_order(n1, n2);
        results.push(result);
    }

    let mut total = 0;
    for i in 0..results.len() {
        if results[i] == Ordering::Less {
            total += i + 1;
        }
    }

    total as i32
}

fn part_2(input: &String) -> i32 {
    let div1 = parse_line("[[2]]");
    let div2 = parse_line("[[6]]");
    div1.borrow_mut().value = -2;
    div2.borrow_mut().value = -2;

    let mut all_lines: Vec<Rc<RefCell<SignalNode>>> = vec![];
    all_lines.push(div1);
    all_lines.push(div2);

    for l in input.lines() {
        if l.is_empty() {
            continue;
        }
        all_lines.push(parse_line(l));
    }
    all_lines.sort_by(|a, b| in_order(Rc::clone(a), Rc::clone(b)));

    let mut div_idxs: Vec<i32> = vec![];
    for (i, l) in all_lines.iter().enumerate() {
        if l.borrow().value == -2 {
            div_idxs.push(i as i32 + 1);
        }
    }
    div_idxs.iter().product()
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}

/*
[[],[[[]],9,[],1],[1,0]]
[[[10,8,0,[4,3],[1,4]],4,[7,5,[9,10,7,10],8]],[8,[[1,5,9,1],6,[10,5],5,[7,1]]],[[0,7,3],[[5],[8,3,0],4]],[4,2]]

*/
