import frontmatter
import sys


def main():
    paper = sys.argv[1]
    with open(paper, "r") as f:
        data = frontmatter.loads(f.read())

    print(data["title"])

if __name__ == "__main__":
    main()
