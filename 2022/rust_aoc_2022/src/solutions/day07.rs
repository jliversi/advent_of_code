use std::cell::RefCell;
use std::rc::Rc;

enum Command {
    CD(String),
    LS,
}

fn s_to_command(s: &str) -> Command {
    match &s[0..2] {
        "cd" => Command::CD(s[3..].to_string()),
        "ls" => Command::LS,
        _ => Command::LS,
    }
}

#[derive(Debug)]
struct DirNode {
    files: Vec<i32>,
    children: Vec<Rc<RefCell<DirNode>>>,
    parent: Option<Rc<RefCell<DirNode>>>,
}

impl DirNode {
    pub fn new() -> DirNode {
        return DirNode {
            files: vec![],
            children: vec![],
            parent: None,
        };
    }

    pub fn add_child(&mut self, new_node: Rc<RefCell<DirNode>>) {
        self.children.push(new_node);
    }

    pub fn add_file(&mut self, file: i32) {
        self.files.push(file);
    }

    pub fn size(&self) -> i32 {
        self.files.iter().sum::<i32>()
            + self.children.iter().map(|x| x.borrow().size()).sum::<i32>()
    }
}

fn build_tree(input: &String) -> Rc<RefCell<DirNode>> {
    let root = Rc::new(RefCell::new(DirNode::new()));
    let mut current = Rc::clone(&root);

    for mut l in input.split("$").skip(2) {
        l = l.trim();
        match s_to_command(l) {
            Command::CD(a) => match &a[0..] {
                ".." => {
                    let current_clone = Rc::clone(&current);
                    current = Rc::clone(current_clone.borrow().parent.as_ref().unwrap());
                }
                _ => {
                    let child = Rc::new(RefCell::new(DirNode::new()));
                    current.borrow_mut().add_child(Rc::clone(&child));
                    child.borrow_mut().parent = Some(Rc::clone(&current));
                    current = child;
                }
            },
            Command::LS => {
                for ls_line in l.lines().skip(1) {
                    match &ls_line[0..3] {
                        "dir" => continue,
                        _ => {
                            let file_size =
                                ls_line.split(" ").next().unwrap().parse::<i32>().unwrap();
                            current.borrow_mut().add_file(file_size);
                        }
                    }
                }
            }
        }
    }
    root
}

fn calc_sizes(root: &Rc<RefCell<DirNode>>) -> Vec<i32> {
    let mut result: Vec<i32> = vec![];
    result.push(root.borrow().size());
    for child in root.borrow().children.iter() {
        result.append(&mut calc_sizes(&child))
    }
    result
}

fn part_1(input: &String) -> i32 {
    let root = build_tree(input);
    let sizes = calc_sizes(&root);
    sizes.iter().filter(|&&x| x < 100000).sum()
}

fn find_pt_2_dir(mut sizes: Vec<i32>) -> i32 {
    const TOTAL_SPACE: i32 = 70000000;
    const NEEDED_SPACE: i32 = 30000000;
    let current_used: i32 = *sizes.iter().max().unwrap();
    let min_to_delete = NEEDED_SPACE - (TOTAL_SPACE - current_used);

    sizes.sort();
    for size in sizes {
        if size > min_to_delete {
            return size;
        }
    }
    1
}

fn part_2(input: &String) -> i32 {
    let root = build_tree(input);
    let sizes = calc_sizes(&root);
    find_pt_2_dir(sizes)
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}

// fn build_tree1(mut root_node: &DirNode, input: &String) {
//     let mut current_node: &DirNode = root_node;
//     let mut new_node;
//     for mut l in input.split("$").skip(1) {
//         l = l.trim();
//         match s_to_command(l) {
//             Command::CD(a) => {
//                 match &a[0..] {
//                     ".." => current_node = &current_node.parent.unwrap(),
//                     _ => {
//                         new_node = DirNode::new();
//                         current_node.add_child(Box::new(new_node));
//                         current_node = &new_node;
//                     }
//                 }
//                 dbg!(current_node);
//             },
//             Command::LS => {

//                 for ls_line in l.lines().skip(1) {
//                     match &ls_line[0..3] {
//                         "dir" => continue,
//                         _ => {

//                         }
//                     }
//                 }
//             }
//         }

//     }
// }

// fn build_tree2(root_node: &mut DirNode, input: &String) {
//     let mut current_node: &mut DirNode = root_node;
//     let mut new_node;
//     for mut l in input.split("$").skip(1) {
//         l = l.trim();
//         match s_to_command(l) {
//             Command::CD(a) => {
//                 match &a[0..] {
//                     ".." => {
//                         current_node = match &current_node.parent {
//                             Some(p) => p.as_mut(),
//                             None => return,
//                         }
//                     },
//                     _ => {
//                         new_node = DirNode::new();
//                         current_node.add_child(Box::new(new_node));
//                         // current_node = &new_node;
//                     }
//                 }
//             },
//             Command::LS => {
//                 for ls_line in l.lines().skip(1) {
//                     match &ls_line[0..3] {
//                         "dir" => continue,
//                         _ => {

//                         }
//                     }
//                 }
//             }
//         }

//     }
// }
