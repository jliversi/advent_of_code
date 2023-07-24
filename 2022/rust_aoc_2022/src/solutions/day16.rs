use std::collections::HashSet;
use std::collections::HashMap;
use itertools::Itertools;

use queues::*;

#[derive(Debug)]
struct Graph<'a> {
    nodes: Vec<Node<'a>>,
}

#[derive(Debug)]
struct Node<'a> {
    children: Vec<usize>, // vector of indexes in the owning Graph
    name: &'a str,
    value: i32,
}

fn parse_line(l: &str) -> Vec<&str> {
    let split_parts: [&str; 5] = [
        "Valve ",
        " has flow rate=",
        "; tunnels lead to valves ",
        "; tunnel leads to valve ",
        ", ",
    ];
    let str_parts: Vec<&str> = l
        .split(split_parts[0])
        .flat_map(|x| x.split(split_parts[1]))
        .flat_map(|x| x.split(split_parts[2]))
        .flat_map(|x| x.split(split_parts[3]))
        .flat_map(|x| x.split(split_parts[4]))
        .skip(1)
        .collect();

    str_parts
}

fn parse_input(input: &str) -> Graph {
    let mut result = Graph { nodes: vec![] };
    let mut names: Vec<&str> = vec![];

    let p_lines = input.lines().map(parse_line).collect::<Vec<Vec<&str>>>();
    for l in p_lines.iter() {
        let name = l[0];
        let value = l[1].parse::<i32>().unwrap();
        let n = Node {
            name,
            value,
            children: vec![],
        };
        names.push(name);
        result.nodes.push(n);
    }

    for (i, l) in p_lines.iter().enumerate() {
        let n = &mut result.nodes[i];
        for name in l[2..].iter() {
            let name_i = names.iter().position(|x| x == name);
            n.children.push(name_i.unwrap());
        }
    }

    result
}

fn calc_dist(n1_i: usize, n2_i: usize, g: &Graph) -> i32 {
    let n = &g.nodes[n1_i];
    let mut n_q: Queue<(&usize, i32)> = queue![];
    let mut visited = HashSet::from([n1_i]);
    for i in n.children.iter() {
        n_q.add((i, 1)).unwrap();
    }
    while let Ok((i, dist)) = n_q.remove() {
        visited.insert(*i);
        if *i == n2_i {
            return dist;
        } else {
            let new_children = &g.nodes[*i].children;
            for c_i in new_children {
                if !visited.contains(c_i) {
                    n_q.add((c_i, dist + 1)).unwrap();
                }
            }
        }
    }
    -1
}

fn calc_dists(g: &Graph) -> Vec<Vec<i32>> {
    let mut result = vec![];
    for n1_i in 0..g.nodes.len() {
        let mut row = vec![];
        for n2_i in 0..g.nodes.len() {
            let dist = calc_dist(n1_i, n2_i, &g);
            row.push(dist);
        }
        result.push(row);
    }

    


    result
}

fn find_best_path(g: &Graph, s: usize, dists: &Vec<Vec<i32>>) -> i32 {
    let mut result = 0;
    let mut rel_nodes: Vec<usize> = vec![];
    for i in 0..g.nodes.len() {
        if g.nodes[i].value > 0 {
            rel_nodes.push(i);
        }
    }
    

    for p in rel_nodes.iter().permutations(rel_nodes.len()).unique() {

        let mut path: Vec<usize> = vec![0];
        let mut other_stuff = p.into_iter().map(|x| x.to_owned()).collect::<Vec<usize>>();
        path.append(&mut other_stuff);
        let score = calc_path(path, dists, g);
        if score > result {
            result = score;
        }
    }

    result
}
fn calc_path(o: Vec<usize>, dists: &Vec<Vec<i32>>, g: &Graph) -> i32 {
    let mut steps = 30 - dists[o[0]][o[1]];
    let mut total = 0;
    for i in 1..o.len() {
        let val = g.nodes[o[i]].value;
        steps = steps - 1;
        total += val * steps;
        if i < o.len() - 1 {  
            steps = steps - dists[o[i]][o[i + 1]];
        }
    }
    total
}

fn part_1(input: &String) -> i32 {
    let graph = parse_input(input);
    let start = graph.nodes.iter().position(|x| x.name == "AA").unwrap();
    let dists = calc_dists(&graph);
    // let mut visits = vec![];

    dbg!(vec![vec![0usize; 0]; 10]);
    // let a = find_best_path(&graph, start, &dists);
    // let best_path = calc_best_path(&graph, start, &dists, &ignores, &mut visits, 30, 0);
    // let a = calc_path(vec![0, 3, 1, 9, 7, 4, 2], &dists, &graph);

    let mut valves = Vec::<(&str, u16, Vec<&str>)>::new();
    for line in input.trim().split('\n') {
        let (valve, flow, _, tunnels) = sscanf::sscanf!(
            line,
            "Valve {str} has flow rate={u16}; {str:/tunnels? leads? to valves?/} {str}"
        )
        .unwrap();
        let tunnels = tunnels.split(", ").collect::<Vec<_>>();
        valves.push((valve, flow, tunnels));
    }

    // compute indices so that valves with positive flow have indices 0..m
    valves.sort_by(|a, b| b.1.cmp(&a.1));
    let lab2idx = valves
        .iter()
        .enumerate()
        .map(|(i, v)| (v.0, i))
        .collect::<HashMap<_, _>>();
    let m = valves.iter().filter(|v| v.1 > 0).count();
    let n = valves.len();
    let mut adj = vec![vec![0usize; 0]; n];
    let mut flow = vec![0u16; n];
    for v in valves.iter() {
        let i = lab2idx[v.0];
        flow[i] = v.1;
        for w in v.2.iter() {
            adj[i].push(lab2idx[w]);
        }
    }
    let a = 1 << (18 as usize);
    dbg!(a);
    1

}

fn part_2(input: &String) -> i32 {
    1
}

pub fn solve(input: String) {
    println!("Part 1 solution: {}", part_1(&input));
    println!("Part 2 solution: {}", part_2(&input));
}
