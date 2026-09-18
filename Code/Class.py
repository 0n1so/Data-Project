class Chart:
    Monday = None
    Tuesday = None
    Wednesday = None
    Thursday = None
    Friday = None
    Saturday = None
    Sunday = None

    def number_of_par(self, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday):
        self.Monday = Monday
        self.Tuesday = Tuesday
        self.Wednesday = Wednesday
        self.Thursday = Thursday
        self.Friday = Friday
        self.Saturday = Saturday
        self.Sunday = Sunday

    def all_charts(self):
        return f"Monday: {self.Monday}, Tuesday: {self.Tuesday}, Wednesday: {self.Wednesday}, Thursday: {self.Thursday}, Friday: {self.Friday}, Saturday: {self.Saturday}, Sunday: {self.Sunday}"

Zaymenik = Chart()
Zaymenik.number_of_par(2, 3, 4, 3, 2, 0, 0)

Chislivnik = Chart()
Chislivnik.number_of_par(1, 2, 3, 1, 2, 0, 0)

print("Zaymenik: " + Zaymenik.all_charts())
print("Chislivnik: " + Chislivnik.all_charts())