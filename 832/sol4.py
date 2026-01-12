class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            row = image[i][::-1]
            for j in range(len(row)):
                row[j] ^= 1
            image[i] = row
        return image
