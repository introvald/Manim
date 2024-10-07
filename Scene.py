from manim import *

class NeuralNetwork(Scene):
    def construct(self):
        # Create layers
        input_layer = VGroup(*[Dot() for _ in range(3)]).arrange(DOWN, buff=0.5)
        hidden_layer = VGroup(*[Dot() for _ in range(4)]).arrange(DOWN, buff=0.5)
        output_layer = VGroup(*[Dot() for _ in range(2)]).arrange(DOWN, buff=0.5)

        # Position layers
        input_layer.move_to(LEFT * 3)
        hidden_layer.move_to(ORIGIN)
        output_layer.move_to(RIGHT * 3)

        # Create edges
        edges = VGroup()
        for input_node in input_layer:
            for hidden_node in hidden_layer:
                edges.add(Line(input_node.get_center(), hidden_node.get_center()))
        for hidden_node in hidden_layer:
            for output_node in output_layer:
                edges.add(Line(hidden_node.get_center(), output_node.get_center()))

        # Add layers and edges to the scene
        self.play(Create(input_layer), Create(hidden_layer), Create(output_layer))
        self.play(Create(edges))

        # Add labels
        input_label = Text("Input Layer").next_to(input_layer, UP)
        hidden_label = Text("Hidden Layer").next_to(hidden_layer, UP)
        output_label = Text("Output Layer").next_to(output_layer, UP)
        self.play(Write(input_label), Write(hidden_label), Write(output_label))

if __name__ == "__main__":
    from manim import *
    config.media_width = "75%"
    scene = NeuralNetwork()
    scene.render()
