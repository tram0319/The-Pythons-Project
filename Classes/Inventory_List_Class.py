from Video_Class import Video
import re
import json

class Inventory_List():

    def __init__(self):
        self.inventory_list = []
        self.read_inventory()

    def read_inventory(self):
        with open("inventory.json", "r") as f:
            # Load the JSON data from the file
            data = json.load(f)
            # Create a new Video object for each item in the JSON data
            for item in data:
                new_video = Video(item['name'], item['year'], item['director'], item['rating'], item['genre'],
                                  item['rentalStatus'])
                # Add the new Video object to the inventory_list
                self.inventory_list.append(new_video)

    def get_inventory(self):
        return self.inventory_list

    def add_video(self, name, year, director, rating, genre, rentalStatus):
        if re.match("^[a-zA-Z ]+$", director) and year.isnumeric():
            new_video = Video(name, year, director, rating, genre, rentalStatus)
            self.inventory_list.append(new_video)
            return f'Added: {name} to inventory.'
        elif not re.match("^[a-zA-Z ]+$", director):
            return f'Video director name cannot contain digits'
        elif not year.isnumeric():
            return f'Video year must only contain digits'
        else:
            return f'An error occurred while adding {name} to inventory.'

    def remove_video(self, name):
        for video in self.inventory_list:
            if video.name == name:
                self.inventory_list.remove(video)
                return f'Removed: {name} from inventory.'
        return 'Video not found in inventory'

    def get_video(self, name):
        for video in self.inventory_list:
            if video.name == name:
                return video
        return f'Video was not found in inventory'

    def get_inventory_list_by_attribute(self, attribute):
        matching_inventory = []
        for video in self.inventory_list:
            if attribute in video.name or attribute in video.genre or attribute in str(
                    video.year) or attribute in video.director or attribute in str(video.rating):
                matching_inventory.append(video)
        return matching_inventory

    def sort_inventory(self, attribute, order='asc'):
        reverse = False if order == 'asc' else True
        self.inventory_list.sort(key=lambda x: getattr(x, attribute), reverse=reverse)

    def write_inventory(self):
        with open("inventory.json", "w") as f:
            # Convert the object to a JSON serializable format
            serializable_list = [video.__dict__ for video in self.inventory_list]
            # Write the JSON serializable object to the file
            json.dump(serializable_list, f)
