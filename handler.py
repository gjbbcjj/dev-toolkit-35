from typing import Any, Dict, Tuple

class RequestHandler:
    """
    Handles incoming requests and processes them according to the specified action.
    """

    def __init__(self, action: str) -> None:
        """
        Initializes the RequestHandler with an action type.
        
        :param action: The action to be performed by this handler.
        """
        self.action = action

    def process_request(self, data: Dict[str, Any]) -> Tuple[str, Dict[str, Any]]:
        """
        Processes the incoming request based on the action.
        
        :param data: The input data for processing.
        :return: A tuple containing a status message and the processed data.
        """
        # Simulate request processing
        processed_data = {key: value for key, value in data.items()}
        return (f'Request processed for action: {self.action}', processed_data)

    def get_action(self) -> str:
        """
        Returns the current action of the handler.
        
        :return: The action name.
        """
        return self.action

# Example of using the RequestHandler
if __name__ == '__main__':
    handler = RequestHandler('example_action')
    response = handler.process_request({'key1': 'value1', 'key2': 'value2'})
    print(response)