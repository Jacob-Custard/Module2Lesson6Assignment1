# Task 1 Keyword Highlighter: Write a program that searches through the reviews list and looks for keywords such as "good",
#"excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each
#review with the keywords in uppercase so they stand out.

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

keywords = ["good", "Good", "excellent", "Excellent", "bad", "Bad", "poor", "Poor", "average", "Average"]

for review in reviews:
    for keyword in keywords:
        if keyword in review:
            index = review.find(keyword)
            new_keyword = keyword.upper()
            if index == 0:
                new_review = (new_keyword + review[len(keyword):] )
                print(new_review)
            else:
                new_review = (review[:index] + new_keyword + review[index + len(keyword):])
                print(new_review)

        else:
            continue      


# Task 2 Sentiment Tally: Develop a function that tallies the number of positive and negative words in each review.
#The function should return the total count of positive and negative words.            
        
def pos_neg_word_count(text): 
    positive_words = ["good", "Good", "excellent", "Excellent", "great", "Great", "awesome", "Awsome", "fantastic", "Fantastic", "superb", "Superb", "amazing", "Amazing"]
    negative_words = ["bad", "Bad", "poor", "Poor", "terrible", "Terrible", "horrible", "Horrible", "awful", "Awful", "disappointing", "Disappointing", "subpar", "Subpar"]
    pos_word_count = []
    neg_word_count = []

    for word in positive_words:
        pos_count = text.count(word)
        pos_word_count.append(pos_count)

    for word in negative_words:
        neg_count = text.count(word)
        neg_word_count.append(neg_count)

    complete_count = neg_word_count + pos_word_count
    total_count = sum(complete_count)
    return total_count


for review in reviews:
    complete_word_count = pos_neg_word_count(review)
    print(complete_word_count)


# Task 3 Review Summary: Implement a script that takes the first 30 characters of a review and appends "..." to create a summary.
#Ensure that the summary does not cut off in the middle of a word.

def review_summary(text):

    new = " ".join(text[:31].split(" ") [0:-1]) + "..."
    return new

for review in reviews:
    summary = review_summary(review)
    print(summary)











