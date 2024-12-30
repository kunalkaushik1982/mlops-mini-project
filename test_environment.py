# import sys

# REQUIRED_PYTHON = "python3"


# def main():
#     system_major = sys.version_info.major
#     if REQUIRED_PYTHON == "python":
#         required_major = 2
#     elif REQUIRED_PYTHON == "python3":
#         required_major = 3
#     else:
#         raise ValueError("Unrecognized python interpreter: {}".format(
#             REQUIRED_PYTHON))

#     if system_major != required_major:
#         raise TypeError(
#             "This project requires Python {}. Found: Python {}".format(
#                 required_major, sys.version))
#     else:
#         print(">>> Development environment passes all tests!")


# if __name__ == '__main__':
#     main()
# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("anandshaw2001/chatgpt-users-reviews")

# print("Path to dataset files:", path)

# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("srisaisuhassanisetty/fake-job-postings")

# print("Path to dataset files:", path)

# import kagglehub

# # Download latest version
# path = kagglehub.dataset_download("kashishparmar02/social-media-sentiments-analysis-dataset")

# print("Path to dataset files:", path)

import kagglehub

# Download latest version
path = kagglehub.dataset_download("nicapotato/womens-ecommerce-clothing-reviews")

print("Path to dataset files:", path)