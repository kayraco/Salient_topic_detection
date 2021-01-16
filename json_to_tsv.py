import argparse
import json
import csv


def get_post(json_data, out_file):
    data = []

    for posts in json_data:
        row = {}
        row["Name"] = posts["data"]["name"]
        row["title"] = posts["data"]["title"]
        row["coding"] = ""
        row["mentioned_candidate"] = ""
        row["upvote_ratio"] = posts["data"]["upvote_ratio"]
        row["ups"] = posts["data"]["ups"]
        row["score"] = posts["data"]["score"]
        row["num_comments"] = posts["data"]["num_comments"]
        row["total_awards_received"] = posts["data"]["total_awards_received"]
        data.append(row)

    csv_columns = ['Name', 'title', 'coding', 'mentioned_candidate', 'upvote_ratio', 'ups', 'score', 'num_comments', 'total_awards_received']
    csv_filename = out_file

    with open(csv_filename, 'w') as csvfile:
        dict_writer = csv.DictWriter(csvfile, csv_columns, delimiter='\t')
        dict_writer.writeheader()
        dict_writer.writerows(data)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('-o', '--out_file', help='output filepath in a tsv format')
    parser.add_argument('json_file', help='the path to file that contains posts')
    parser.add_argument('num_posts_to_output', nargs='?', help='number of posts to output')
    args = parser.parse_args()
    out_file = args.out_file

    with open(args.json_file, 'r') as handle:
        json_data = [json.loads(line) for line in handle]

    get_post(json_data, out_file)


if __name__ == '__main__':
    main()
