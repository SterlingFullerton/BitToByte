# Example file showing a basic pygame "game loop"
import pygame
import pygame.surface
from consts import colors, screen_width, screen_height, click_cooldown, images, normal_text_size, normal_padding
from skill import Skill
from buttons import Button
import random

screen_dimensions = (screen_width, screen_height)

#Center of the screen
cos = (screen_width // 2, screen_height // 2)

# pygame setup
pygame.init()
screen = pygame.display.set_mode(screen_dimensions)
clock = pygame.time.Clock()
running = True

#Joshes Awesome Globals
skill_queue = []
streak = 0
all_questions = []

# Not Joshes Globals
num_combined = "00000"
num_binary = 0
num_final = random.randint(0, 31)

pygame.display.set_caption("BitToByte: Discover Computers!")

# Load Assets
assets = {}
for image in images:
    assets[image] = pygame.image.load(images[image])


# Scale the logo down
logo1_rect = assets["logo1"].get_rect()
assets["logo1"] = pygame.transform.scale(assets["logo1"], (logo1_rect.width // 2, logo1_rect.height // 2))

# Init Skill Tree
skills = {}
skills["Test Skill 1"] = Skill(
    name="Test Skill 1",
    prerequisites=[],
    x=cos[0],
    y=cos[1],
    icon_color=colors["neon_green"],
    icon=assets["code"]
)
skills["Test Skill 2"] = Skill(
    name="Test Skill 2",
    prerequisites=["Test Skill 1"],
    x=cos[0] + 50,
    y=cos[1] + 50
)
skills["Test Skill 3"] = Skill(
    name="Test Skill 3",
    prerequisites=["Test Skill 1"],
    x=cos[0] - 50,
    y=cos[1] - 50
)
skills["Test Skill 4"] = Skill(
    name="Test Skill 4",
    prerequisites=["Test Skill 1"],
    x=cos[0] - 50,
    y=cos[1] + 50
)
skills["Test Skill 5"] = Skill(
    name="Test Skill 5",
    prerequisites=["Test Skill 1"],
    x=cos[0] + 50,
    y=cos[1] - 50
)

# Init Buttons
main_menu_buttons = {
    "Start Learning": {
        "B": 
            Button(
                x=cos[0],
                y=cos[1],
                text="Start Learning",
                text_size=24,
                rounded=True,
                radius=10,
                border=True,
                border_width=2,
                padding=30
            ),
        "D": "skill_tree"
    }
}
mc_buttons = {
    "Button1":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button1",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30
        ),
    "Button2":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button2",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30
        ),
    "Button3":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button3",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30
        ),
    "Button4":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button4",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30
        ),
}
fb_buttons = {
    "Button1": 
        Button(
            x=cos[0],
            y=cos[1],
            text="Button1",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            immutable_size=True
        ),
    "Button2":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button2",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            immutable_size=True
        ),
    "Button3":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button3",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            immutable_size=True
        ),
    "Button4":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button4",
            text_size=24,
            width=200,
            height=50,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            immutable_size=True
        ),
}

robs_buttons = {
    "Button1":
        Button(
            x=23,
            y=60,
            text="1",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 0,
            immutable_size=True
        ),
    "Button2":
        Button(
            x=151,
            y=60,
            text="2",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 1,
            immutable_size=True
        ),
    "Button3":
        Button(
            x=280,
            y=60,
            text="3",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 2,
            immutable_size=True
        ),
    "Button4":
        Button(
            x=23,
            y=205,
            text="4",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 3,
            immutable_size=True
        ),
    "Button5":
        Button(
            x=151,
            y=205,
            text="5",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 4,
            immutable_size=True
        ),
    "Button6":
        Button(
            x=280,
            y=205,
            text="6",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 5,
            immutable_size=True
        ),
    "Button7":
        Button(
            x=23,
            y=350,
            text="7",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 6,
            immutable_size=True
        ),
    "Button8":
        Button(
            x=151,
            y=350,
            text="8",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 7,
            immutable_size=True
        ),
    "Button9":
        Button(
            x=280,
            y=350,
            text="9",
            text_size=24,
            width=110,
            height=125,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=30,
            icon = images['eyeClosed'],
            index = 8,
            immutable_size=True
        ),
}

binary_conversion_buttons = {
    "Button1":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button1",
            text_size=40,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=45,
            immutable_size=True,
            immutable_pos=True
        ),
    "Button2":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button2",
            text_size=40,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=45,
            immutable_size=True,
            immutable_pos=True
        ),
    "Button3":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button3",
            text_size=40,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=45,
            immutable_size=True,
            immutable_pos=True
        ),
    "Button4":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button4",
            text_size=40,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=45,
            immutable_size=True,
            immutable_pos=True
        ),
    "Button5":
        Button(
            x=cos[0],
            y=cos[1],
            text="Button5",
            text_size=40,
            rounded=True,
            radius=10,
            border=True,
            border_width=2,
            padding=45,
            immutable_size=True,
            immutable_pos=True
        ),
}
back_button = Button(
        x=50,
        y=60,
        text="Back",
        text_size=24,
        rounded=True,
        radius=10,
        border=True,
        border_width=2,
        padding=20
    )

def click_button(rectangle, button=[0]):
    # The default button list is a persistent list that will store the cooldown of the button

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Only let a button be clicked every click_cooldown frames
    if rectangle.collidepoint(mouse) and click[0] == 1 and button[0] == 0:
        button[0] = click_cooldown
        return True
    
    # If the button is clicked, decrease the button cooldown
    if button[0] > 0:
        button[0] -= 1
    
    return False

def main_menu():
    global current_screen

    # Draw the logo
    screen.blit(assets["logo1"], 
        (
            screen_width // 2 - assets["logo1"].get_width() // 2, 
            screen_height // 6
        )
    )
    
    for button in main_menu_buttons.values():
        # Draw the buttons
        button["B"].draw(screen)

        # Check for button click
        if click_button(button["B"].rectangle):
            print("Button Clicked")
            current_screen = button["D"]

def skill_tree():
    global current_screen, question, answers, correct_answer

    # Draw lines connecting the skills
    pygame.draw.line(screen, colors["grey_text"], (cos[0], cos[1]), (cos[0] + 50, cos[1] + 50), 2)
    pygame.draw.line(screen, colors["grey_text"], (cos[0], cos[1]), (cos[0] - 50, cos[1] - 50), 2)
    pygame.draw.line(screen, colors["grey_text"], (cos[0], cos[1]), (cos[0] - 50, cos[1] + 50), 2)
    pygame.draw.line(screen, colors["grey_text"], (cos[0], cos[1]), (cos[0] + 50, cos[1] - 50), 2)

    for skill in skills.values():
        skill.draw(screen)

    for skill in skills.values():
        if skill.check_hover(pygame.mouse.get_pos()):
            skill.display_name(screen)

        # questionNum = 1 #random.randint(0,1)
        # if click_button(skill.circle):
        #     current_screen = all_questions[questionNum][0]
        #     question = all_questions[questionNum][1]
        #     answers = [all_questions[questionNum][2],all_questions[questionNum][3],all_questions[questionNum][4],all_questions[questionNum][5]]
        #     correct_answer = all_questions[questionNum][6]

        if click_button(skill.circle):
            current_screen = all_questions[questionNum][0]
            question = all_questions[questionNum][1]
            answers = [all_questions[questionNum][2],all_questions[questionNum][3],all_questions[questionNum][4],all_questions[questionNum][5]]
            correct_answer = all_questions[questionNum][6]

        #if click_button(skill.circle):
         #   current_screen = "fill_in_the_blank"
          #  question = "What is the capital of France?"
           # answers = ["Paris", "London", "Berlin", "Madrid"]
            #correct_answer = "Paris"

# Game Options
def fill_in_the_blank():
    global last_screen
    
    #Init
    if last_screen != "fill_in_the_blank":
        tempIndex = 0
        for button in fb_buttons.values():
            button.setNewText(answers[tempIndex])
            button.setSize(200, 50)
            button.setNewPos(cos[0], cos[1] + tempIndex * 60)
            tempIndex += 1

    # Display Question
    font = pygame.font.Font(None, normal_text_size)
    question_label = font.render(question[0] + '_ _ _' + question[1], True, colors["grey_text"])
    screen.blit(question_label, (screen_width // 2 - question_label.get_width() // 2, screen_height // 6))

    # Drop Rectangle
    r = pygame.draw.rect(screen, colors["grey_text"], (screen_width // 2 - 100, screen_height // 2 - 200, 200, 50), 2)
    
    for button in fb_buttons.values():
        # Draw the buttons
        button.draw(screen)

        # Check for button click
        if click_button(button.rectangle):
            if button.attached():
                # Check if the cursor is colliding with the text box (r)
                # If it is, then set the button to the correct position
                mouse = pygame.mouse.get_pos()
                if r.collidepoint(mouse):
                    button.setNewPos(r.x + r.width // 2, r.y + r.height // 2)
                    print("Correct Answer")
                    #skill_queue.pop(0)
                else:
                    print("Incorrect Answer")
                    #skill_queue.append()
                
                button.detach()
            else:
                button.attach()

def multiple_choice():
    global last_screen
    #Screen initialization
    if last_screen != "multiple_choice":
        tempIndex = 0
        for button in mc_buttons.values():
            button.setNewText(answers[tempIndex])
            button.setSize(200, 50)
            button.setNewPos(cos[0], cos[1] + tempIndex * 60)
            tempIndex += 1
    
    font = pygame.font.Font(None, normal_text_size)
    question_label = font.render(question, True, colors["grey_text"])
    screen.blit(question_label, (screen_width // 2 - question_label.get_width() // 2, screen_height // 6))

    for button in mc_buttons.values():
        # Draw the buttons
        button.draw(screen)

        # Check for button click
        if click_button(button.rectangle):
            #Check selection
            if button.str_text == correct_answer:
                button.border_color = colors["neon_green"]
                print("Right Answer")
                #skill_queue.pop(0)
            else:
                button.border_color = colors["red"]
                print("Wrong Answer")
                # skill_queue.append()
    pass


def tower_of_terry():
    
    pass


def robs_sorting_scheme():

    pass

def read_csv(file_path):
    with open(file_path, newline='') as file:
        for line in file.readlines():
            sections = [x.strip() for x in line.split(',')]

            if sections[0] == 'fill_in_the_blank':
                sections[1] = [sections[1], sections.pop(2)]

            all_questions.append(sections)


read_csv("stupidDataThatRobShouldaMadeByNow.csv")
current_screen = "main_menu"
last_screen = ""

# Questions and Answers
# question = "What is the capital of France?"
# answers = ["Paris", "London", "Berlin", "Madrid"]
# correct_answer = "Paris"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(colors["black"])

    # Draw the background
    screen.blit(assets["background"], (0, 0))

    if current_screen == "main_menu":
        main_menu()
        last_screen = "main_menu"
    elif current_screen == "skill_tree":
        skill_tree()
        last_screen = "skill_tree"
    elif current_screen == "fill_in_the_blank":
        fill_in_the_blank()
        last_screen = "fill_in_the_blank"
    elif current_screen == "multiple_choice":
        multiple_choice()
        last_screen = "multiple_choice"
    else:
        print("Invalid Screen")
        exit()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

# Do a backflip