from typing import List, Tuple

class DataProcessor:
    def __init__(self, data: List[Tuple[int, float]]) -> None:
        """
        Initializes the DataProcessor with a list of data.
        
        :param data: A list of tuples where each tuple contains an integer and a float.
        """
        self.data = data

    def average(self) -> float:
        """
        Calculates the average of the float values in the data.
        
        :return: The average as a float.
        """  
        if not self.data:
            return 0.0
        total = sum(value for _, value in self.data)
        return total / len(self.data)

    def filter_above_threshold(self, threshold: float) -> List[Tuple[int, float]]:
        """
        Filters the data for entries where the float value exceeds the threshold.
        
        :param threshold: The threshold value to filter by.
        :return: A list of tuples that exceed the threshold.
        """  
        return [entry for entry in self.data if entry[1] > threshold]

    def sum_values(self) -> float:
        """
        Sums up the float values in the data.
        
        :return: The total sum as a float.
        """  
        return sum(value for _, value in self.data)  

# Example usage:
if __name__ == '__main__':
    data = [(1, 10.5), (2, 20.1), (3, 5.5)]
    processor = DataProcessor(data)
    print(processor.average())  # Output average
    print(processor.filter_above_threshold(15.0))  # Output filtered data
    print(processor.sum_values())  # Output total sum
