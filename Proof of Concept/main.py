from tools.ingest import load_article
from tools.extract_entities import extract_entities
from tools.graph_builder import update_graph, show_graph


def main():
    a_s = input("analyse or show [a/s]")
    if a_s == 'a':
        source = input("Enter a URL or path to local PDF: ").strip()

        print("Loading content")
        text = load_article(source)

        print("Extracting entities...")
        entities = extract_entities(text)
        print(entities)

        print("Updating graph...")
        update_graph(entities)

        print("Graph updated with extracted entities.")

        show = input("🔎 Do you want to view the graph? (y/n): ").strip().lower()
        if show == "y":
            show_graph()
    if a_s == 's':
        show_graph()

if __name__ == "__main__":
    main()

