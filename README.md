# The World Today — Tuesday 24 November 2026

A one-page newspaper front page summing up the world news of
**Tuesday 24 November 2026**, rendered as a single 1024×1024 image.

## What is in the picture

- **Lead story — "Huang is back":** Jensen Huang was reinstated as chief
  executive of Nvidia less than two weeks after resigning. Vice President
  JD Vance lobbied the board at President Trump's behest, and Mr Trump
  said he convinced the company to bring its founder back. Shares jumped
  on the news.
- **Iran:** Tehran vows to use "all its tools" against the US naval
  blockade, as Vance and Secretary of State Marco Rubio met Qatar's prime
  minister at the White House.
- **Gaza:** An Israeli air strike on Gaza City killed Naeem Abu Nahal,
  director of Hamas' internal security apparatus, and six others, despite
  a ceasefire in place since last year.
- **Ukraine:** An overnight Russian attack on Zaporizhzhia killed two
  people and wounded 40, including four children, after striking an
  apartment building.
- **Space:** NATO chief Mark Rutte vowed the alliance would defend
  against any threat in space, after reports Russia could launch a
  nuclear-armed satellite before the end of the year.
- **Korea:** A suspected North Korean aircraft breached South Korean
  airspace near the island of Ulleung, prompting residents to shelter.
- **In brief:** Trump awards Rudy Giuliani the Medal of Freedom; the US,
  Mexico, Costa Rica and Jamaica will host the 2031 Women's World Cup;
  Honda recalls 810,000 vehicles in the US; a magnitude 5.4 earthquake
  hit Nepal.

All stories are real events reported on 24 November 2026 (AP, Reuters,
BBC, Just Security, SCMP, Times of India).

## How to run

```bash
python3 main.py
```

This writes `entry.png` (1024×1024) in the same directory. The program is
fully deterministic — no network access, no clock, no randomness — so
running it twice produces a byte-identical file. It only needs Pillow and
the DejaVu fonts shipped with most Linux systems.

## Files

- `main.py` — the program that draws the front page
- `entry.png` — the rendered front page
- `LICENSE` — MIT

## Bounty

Built for the make.fun bounty
[news-image-20261124](https://make.fun/bounty/news-image-20261124):
"Sum up 24 November's world news in one image".
